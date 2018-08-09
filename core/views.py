from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt
from django.shortcuts import redirect

import json

from avaliador.models import Avaliador
from dispositivo.DispositivoBase import DispositivoClass
from dispositivo.models import Dispositivo

def index(request):
    dispositivoClass = DispositivoClass()
    context = dispositivoClass.get_list_dados_all()
    return render(request, 'index.html', context)

def devolverDispositivo(request):
    avaliador = Avaliador.objects.filter(user=request.user.id)
    context = {}
    if avaliador[0].dispositivo:
        dispositivo = Dispositivo.objects.filter(pk=avaliador[0].dispositivo.id)
        dispositivo.update(uso=False)
        avaliador.update(dispositivo=None)

    return redirect('/index/')


def selecionarDispositivo(request):
    if request.is_ajax():
        avaliador = Avaliador.objects.filter(user=request.user.id)
        dispositivo = Dispositivo.objects.filter(codigo=request.POST['dispositivo'])
        dispositivo.update(uso=True)
        avaliador.update(dispositivo=dispositivo[0])
        return HttpResponse(json.dumps({'ok':True, 'msg': "Sucesso!"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'ok':False, 'msg': "Algo deu errado!"}), content_type="application/json")


def red(request):
    client = mqtt.Client(client_id=str(request.user), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
    client.connect( "192.168.1.200", 1883, 60)
    client.subscribe("device/1/code")
    client.publish("device/1/code", payload="RED", qos=0, retain=False)
    return render(request, "index.html")

def blue(request):
    # client = mqtt.Client(client_id=str(request.user), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
    # client.connect( "192.168.1.200", 1883, 60)
    # client.subscribe("device/2/code")
    # client.publish("device/2/code", payload="BLUE", qos=0, retain=False)
    return render(request, "index.html")

def tone(request):
    client = mqtt.Client(client_id=str(request.user), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
    client.connect( "192.168.1.200", 1883, 60)
    client.subscribe("device/3/code")
    client.publish("device/3/code", payload="TONE", qos=0, retain=False)
    return render(request, "index.html")

def green(request):
    client = mqtt.Client(client_id=str(request.user), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
    client.connect( "192.168.1.200", 1883, 60)
    client.subscribe("device/2/code")
    client.publish("device/2/code", payload="GREEN", qos=0, retain=False)
    return render(request, "index.html")
