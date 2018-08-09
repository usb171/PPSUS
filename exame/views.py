import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import ExameForm
from django.contrib.auth.models import User
from avaliador.models import Avaliador
from paciente.models import Paciente
from exame.models import Exame #, TipoExame
from tipoExame.models import TipoExame
# from tipoExame.forms import TipoExameForm
from coleta.models import Coleta
from django.http import JsonResponse, HttpResponse
# from coleta.views import RegistrarColetaView
import json

from paciente.PacienteBase import PacienteClass
from exame.ExameBase import ExameClass

import locale
from datetime import datetime
#locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

id_tipo_exame_buffer = None

pacienteClass = PacienteClass()
exameClass = ExameClass()

# template_novo_tipo_exame = "exame/novoTipoExame.html"

def detail(request, id=None):
    instance = get_object_or_404(Coleta, id=id)
    context = {
        "fk_tipoExame": instance.tipoExame.nomeExame.replace('_',' '),
        "fk_paciente": instance.paciente.nomeCompleto.replace('_',' '),
        "dataCriacao": instance.dataCriacao,
        "observacao":  instance.observacao,
        "riscoQueda": instance.riscoQueda,
        "id": instance.id,
        #"observacao": instance.observacao
    }
    return render(request, "exame/editarExame.html", context)

def editarExame(request):
    if request.is_ajax() and not request.POST.get('flag_exame'):
        coleta = Coleta.objects.filter(pk=request.POST['exame_coleta'])
        coleta.update(visivel=False)
        return HttpResponse(json.dumps({'ok':True, 'msg': "Exame Editado com Sucesso!"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'ok':True, 'msg': "Exame Editado com Sucesso!"}), content_type="application/json")


# def novoTipoExame(request):
#     if request.method == 'GET':
#         return render(request, "tipoExame/novoTipoExame.html")
#     elif request.method == 'POST':
#         form = TipoExameForms(request.POST)
#         if form.is_valid():
#             dados = form.cleaned_data
#             tipo_exame = TipoExame.objects.create(nomeExame=dados['nomeExame'].replace(" ", "_").lower())
#             tipo_exame.save()
#             return redirect('index')
#         else:
#             print("Erros: ", form.errors.as_data())
#             return render(request, template_novo_tipo_exame, {'form': form})

def novoExameColeta(request):
    if request.method == 'GET':
        return render(request, "exame/editarExame.html")

def get_dados_exame(request):
    paciente_search = request.GET.get('paciente_search', None)
    paciente = None
    if paciente_search.isdigit():
        paciente = Paciente.objects.get(cpf=paciente_search)
    else:
        dic_filtro = pacienteClass.get_dic_nome_codeNome(paciente_search)
        paciente = Paciente.objects.get(nomeCompleto=dic_filtro["nomePaciente"], code_nomeCompleto=dic_filtro["codeNomePaciente"])

    exames = Exame.objects.get(fk_paciente=paciente)

    data = {
        #'exames': list(exames.fk_coleta.all()),
        'dic_exames': exameClass.get_dic_coletas(exames.fk_coleta.all().filter(visivel=True)),
        'id_paciente': paciente.id,
    }
    return JsonResponse(data)

class RegistrarExameView(View):
    template_name = 'exame/novoExame.html'

    def get(self, request):
        context = {}
        context.update({"tipo_exames": TipoExame.objects.all()})
        context.update({"pacientes": Paciente.objects.all().filter(visivel=True)})
        return render(request, self.template_name, context)

    def post(self, request):

        form = ExameForm(request.POST)
        if form.is_valid():
            global id_tipo_exame_buffer;
            dados = form.cleaned_data
            context = {}
            context.update({'nomeCompleto':dados['fk_paciente'][0]})
            context.update({'id_paciente': dados['fk_paciente'][0].id})

            # Reconhece qual button do tipo_exame foi selecionado #################
            for t_e in list(map(lambda t_e: t_e.nomeExame,TipoExame.objects.all())):
                if ('button_' + t_e) in request.POST:
                    id_tipo_exame_buffer = TipoExame.objects.get(nomeExame=t_e).id
                    context.update({'tipoExame':t_e})
                    context.update({'id_tipoExame': id_tipo_exame_buffer})
                    return render(request, "exame/novoExame.html", context)
            #######################################################################

            context.update({'id_tipoExame':id_tipo_exame_buffer})
            id_tipo_exame_buffer = None
            print(dados)
            # exame = Exame.objects.create(fk_paciente=Paciente.objects.get(id=context['id_paciente']),
            #                              fk_tipoExame=TipoExame.objects.get(id=context['id_tipoExame']))
            # exame.save()
            return render(request, 'index.html', context)

        else:
            print("Erros: ", form.errors.as_data())
            return render(request, 'exame/novoExame.html', {'form': form})
