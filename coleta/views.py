from django.shortcuts import render, redirect
from django.views import View
from coleta.forms import ColetaForm, ColetaLaudoForm
from django.http import JsonResponse, HttpResponse
import json

from coleta.models import Coleta
from exame.models import Exame
from paciente.models import Paciente
from tipoExame.models import TipoExame
from avaliador.models import Avaliador

from paciente.PacienteBase import PacienteClass

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from datetime import timedelta
import time

pacienteClass = PacienteClass()

_IP_SERVER = "192.168.1.200"
_DIC_MQTT = {}

def on_start_coleta(client, userdata, msg):
    global _DIC_MQTT
    try:
        if int(msg.payload) >= int(("-80").encode()): # Sinal suficiente para inicar uma coleta
            _DIC_MQTT[str(msg.topic)]['flag_conexao'] = True

    except ValueError:
        if msg.payload == ("C2T").encode(): # Sinal de confirmação que foi iniciado a amostragem
            _DIC_MQTT[str(msg.topic)]['flag_start_coleta'] = True
        else:
            print("Não foi possível iniciar a coleta'")


def on_stop_coleta(client, userdata, msg):
    global _DIC_MQTT
    if msg.payload == ("C3T").encode():
        _DIC_MQTT[str(msg.topic)]['flag'] = False
    else:
        _DIC_MQTT[str(msg.topic)]['amostras'] += str(msg.payload.decode())

    print(str(msg.topic), " ", str(msg.payload.decode()))

def cancelarColeta(request):

    if request.is_ajax():
        return HttpResponse(json.dumps({'ok':True, 'msg': "Coleta Cancelada"}), content_type="application/json")

def iniciarColeta(request):
    global _DIC_MQTT;
    id_avaliador = str(request.user.avaliador.id)
    code_device = str(request.user.avaliador.dispositivo.codigo)
    topico_avaliador_MQTT = "device/"+id_avaliador+"/code"
    topico_dispositivo_MQTT = "device/"+code_device+"/code"
    _DIC_MQTT[topico_avaliador_MQTT] = {'time_out_conexao': 3, 'flag_conexao': False, 'time_out_start_coleta': 5,'flag_start_coleta': False}

    if request.is_ajax():
        client = mqtt.Client(client_id=str(request.user.avaliador.id), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
        client.connect(_IP_SERVER, 1883, 60)
        client.on_message = on_start_coleta
        client.subscribe(topico_avaliador_MQTT)


        while _DIC_MQTT[topico_avaliador_MQTT]['time_out_conexao'] >= 0:
            _DIC_MQTT[topico_avaliador_MQTT]['time_out_conexao'] -= 1
            print(code_device, " Enviando comando C1 ...")
            client.publish(topico_dispositivo_MQTT, payload="C1"+id_avaliador, qos=2, retain=False)
            time.sleep(.1)
            for i in range(5):
                client.loop()
                time.sleep(.3)
            if _DIC_MQTT[topico_avaliador_MQTT]['flag_conexao']: break



        if _DIC_MQTT[topico_avaliador_MQTT]['flag_conexao']:
            print(code_device, " Comando C1 => OK")

            while _DIC_MQTT[topico_avaliador_MQTT]['time_out_start_coleta'] >= 0:
                _DIC_MQTT[topico_avaliador_MQTT]['time_out_start_coleta'] -= 1
                print(code_device, " Enviando comando C2 ...")
                client.publish(topico_dispositivo_MQTT, payload="C2"+id_avaliador, qos=2, retain=False)
                for i in range(5):
                    client.loop()
                    time.sleep(.5)
                if _DIC_MQTT[topico_avaliador_MQTT]['flag_start_coleta']: break



            if _DIC_MQTT[topico_avaliador_MQTT]['flag_start_coleta']:
                print(code_device, " Comando C2 => OK")
                client.disconnect()
                client.loop()
                del client
                return HttpResponse(json.dumps({'ok':True, 'msg': "Coleta Iniciada"}), content_type="application/json")
            else:
                client.disconnect()
                client.loop()
                del client
                return HttpResponse(json.dumps({'ok':False, 'msg': "Dispositivo Desconectado"}), content_type="application/json")

        else:
            client.publish(topico_dispositivo_MQTT, payload="SR", qos=2, retain=False)
            client.loop()
            client.disconnect()
            del client
            return HttpResponse(json.dumps({'ok':False, 'msg': "Dispositivo Desconectado, reiniciando..."}), content_type="application/json")

def finalizarColeta(request):

    global _DIC_MQTT;
    id_avaliador = str(request.user.avaliador.id)
    code_device = str(request.user.avaliador.dispositivo.codigo)
    topico_avaliador_MQTT = "device/"+id_avaliador+"/code"
    topico_dispositivo_MQTT = "device/"+code_device+"/code"

    if request.is_ajax():
        client = mqtt.Client(client_id=id_avaliador, clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
        client.loop()
        client.connect(_IP_SERVER, 1883, 60)
        client.loop()
        client.subscribe(topico_avaliador_MQTT)
        client.loop()
        client.publish(topico_dispositivo_MQTT, payload="C5", qos=2, retain=False)
        for i in range(5): client.loop()
        client.publish(topico_dispositivo_MQTT, payload="C3"+id_avaliador, qos=2, retain=False)
        for i in range(5): client.loop()
        _DIC_MQTT[topico_avaliador_MQTT] = {'amostras': "", 'flag': True}
        client.on_message = on_stop_coleta
        while _DIC_MQTT[topico_avaliador_MQTT]['flag']: client.loop()
        client.publish(topico_dispositivo_MQTT, payload="C4", qos=2, retain=False)
        for i in range(5): client.loop()
        client.disconnect()
        del client
        return HttpResponse(json.dumps({'ok':True, 'msg': "Coleta Finalizada com sucesso"}), content_type="application/json")

# Por JSON retorna os dados do paciente através do id paciente_search
def get_dados_paciente(request):
    dic_json = pacienteClass.get_dic_dados_paciente_search_json(request=request)
    return dic_json
####################################################################

# Por JSON retorna os dados do tipoExame através do id paciente_search
def get_dados_tipo_exame(request):
    tipoExame_search = request.GET.get('tipoExame_search', None)
    tipoExame = TipoExame.objects.get(nomeExame=tipoExame_search)
    nomeExame = tipoExame.nomeExame.replace("_"," ")
    pontuacao_soma = tipoExame.pontuacao_soma
    cronometro = tipoExame.cronometro
    deslocamento = tipoExame.deslocamento
    risco_queda = tipoExame.risco_queda
    coleta_dispositivo = tipoExame.coleta_dispositivo
    pontuacao = tipoExame.pontuacao
    observacao = tipoExame.observacao
    pontuacao_minima = tipoExame.pontuacao_minima
    pontuacao_maxima = tipoExame.pontuacao_maxima

    descricaoExame = tipoExame.descricao
    id = tipoExame.id
    data = {
        'nomeExame': nomeExame,
        'descricaoExame': descricaoExame,
        'id': id,
        'pontuacao_soma': pontuacao_soma,
        'observacao': observacao,
        'cronometro':  cronometro,
        'deslocamento': deslocamento,
        'risco_queda': risco_queda,
        'coleta_dispositivo': coleta_dispositivo,
        'pontuacao': pontuacao,
        'pontuacao_minima': pontuacao_minima,
        'pontuacao_maxima': pontuacao_maxima,
    }
    return JsonResponse(data)
######################################################################

def coletarDados(request):
    print("Coleando dados...")
    return render(request, "index.html")

def salvarLaudo(request):
    if request.is_ajax():
        form = ColetaLaudoForm(request.POST)
        if form.is_valid():
            global _DIC_MQTT
            topico_avaliador_MQTT = "device/"+str(request.user.avaliador.id)+"/code"
            dados = form.cleaned_data
            amostras = None

            if _DIC_MQTT.get(topico_avaliador_MQTT):
                amostras = _DIC_MQTT[topico_avaliador_MQTT]['amostras']
            else:
                amostras = "Não há amostras para esse tipo de exame"

            coleta_id = dados['coleta_id']
            observacao = dados['observacao']
            cronometro = dados['cronometro']
            pontuacao = dados['pontuacao']
            risco_queda = dados['risco_queda']
            deslocamento = dados['deslocamento']
            pontuacao_soma = dados['pontuacao_soma']


            coleta = Coleta.objects.filter(pk=coleta_id)

            coleta.update(observacao=observacao, cronometro=cronometro, deslocamento=deslocamento, pontuacao=pontuacao, pontuacao_soma=pontuacao_soma, riscoQueda=risco_queda, visivel=True, amostras=amostras)

            if topico_avaliador_MQTT in _DIC_MQTT: del _DIC_MQTT[topico_avaliador_MQTT]
            return HttpResponse(json.dumps({'ok':True, 'msg': "Sucesso"}), content_type="application/json")
        else:
            print("Erros: ", form.errors.as_data())
            return HttpResponse(json.dumps({'ok':True, 'msg': form.errors.as_data()}), content_type="application/json")

def novaColeta(request):
    if request.method == 'GET':
        context = {"pacientes": Paciente.objects.all().filter(visivel=True)}
        nome_exames = list(map( lambda t_e: t_e.nomeExame ,TipoExame.objects.all().filter(visivel=True)))
        context.update({"nome_exames": nome_exames})
        context.update({"exames_obj": TipoExame.objects.all().filter(visivel=True)})
        return render(request, 'coleta/novaColeta.html', context)
    elif request.method == 'POST':
        form = ColetaForm(request.POST)
        if request.is_ajax() and form.is_valid():
            dados = form.cleaned_data
            coleta = Coleta.objects.create(paciente_id=dados['paciente'][0].id,tipoExame_id=dados['tipoExame'][0].id)
            coleta.save()
            print("Nova Coleta post: ", coleta)

            exame = Exame.objects.filter(fk_paciente=dados['paciente'][0].id)[0]
            exame.fk_coleta.add(coleta)
            exame.save()

            return HttpResponse(json.dumps({'ok':True, 'msg': "Sucesso", 'id_coleta': coleta.id}), content_type="application/json")
        else:
            erro_msg = form.errors
            mensagem = ""
            n_focus = 0
            if erro_msg.get('tipoExame'):
                mensagem = "Tipo Exame Inválido!"
                n_focus = 1
            if erro_msg.get('paciente'):
                mensagem = "Paciente Inválido!"
                n_focus = 2
            return HttpResponse(json.dumps({'ok':False, 'msg': mensagem, 'focus': n_focus}), content_type="application/json")









def novaFicha(request):
    if request.method == 'GET':
        context = {"pacientes": Paciente.objects.all().filter(visivel=True)}
        nome_exames = list(map( lambda t_e: t_e.nomeExame ,TipoExame.objects.all().filter(visivel=True)))
        context.update({"nome_exames": nome_exames})
        context.update({"exames_obj": TipoExame.objects.all().filter(visivel=True)})
        return render(request, 'coleta/novaFicha.html', context)
    elif request.method == 'POST':
        form = ColetaLaudoForm(request.POST)
        if request.is_ajax() and form.is_valid():
            global _DIC_MQTT
            topico_avaliador_MQTT = "device/"+str(request.user.avaliador.id)+"/code"
            dados = form.cleaned_data
            amostras = None

            if _DIC_MQTT.get(topico_avaliador_MQTT):
                amostras = _DIC_MQTT[topico_avaliador_MQTT]['amostras']
            else:
                amostras = "Não há amostras para esse tipo de exame"

            pontuacao = dados['pontuacao']
            paciente_id = dados['paciente']
            observacao = dados['observacao']
            cronometro = dados['cronometro']
            tipoExame_id = dados['tipoExame']
            risco_queda = dados['risco_queda']
            deslocamento = dados['deslocamento']
            pontuacao_soma = dados['pontuacao_soma']

            coleta = Coleta.objects.create(paciente_id=paciente_id,
                                           tipoExame_id=tipoExame_id,
                                           observacao=observacao,
                                           cronometro=cronometro,
                                           deslocamento=deslocamento,
                                           pontuacao=pontuacao,
                                           pontuacao_soma=pontuacao_soma,
                                           riscoQueda=risco_queda,
                                           visivel=True,
                                           amostras=amostras)


            coleta.save()

            exame = Exame.objects.filter(fk_paciente=paciente_id)[0]
            exame.fk_coleta.add(coleta)
            exame.save()
            if topico_avaliador_MQTT in _DIC_MQTT: del _DIC_MQTT[topico_avaliador_MQTT]
            return HttpResponse(json.dumps({'ok':True, 'msg': "Laudo Salvo com Sucesso!"}), content_type="application/json")
        else:
            print("Erros: ", form.errors.as_data())
            return HttpResponse(json.dumps({'ok':False, 'msg':" Erro ao Salvar Laudo"}), content_type="application/json")
