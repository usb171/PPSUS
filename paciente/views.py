
from django.shortcuts import render, redirect, HttpResponse
from .models import Paciente
from django.http import JsonResponse
from avaliador.models import Avaliador
from exame.models import Exame
from paciente.forms import PacienteForm, DeletarPacienteForm, EditarPacienteForm
from paciente.PacienteBase import PacienteClass

template_novo_paciente = 'paciente/novoPaciente.html'
template_editar_paciente = 'paciente/editarPaciente.html'
template_delete_paciente = 'paciente/deletarPaciente.html'

pacienteClass = PacienteClass()

def deletar_paciente(request):
    if request.method == 'GET':
        context = {"pacientes": Paciente.objects.all().filter(visivel=True)}
        return render(request, template_delete_paciente, context)

    elif request.method == 'POST':
        form = DeletarPacienteForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            nomeCompleto = pacienteClass.processa_string_nome(dados['nomeCompleto'])
            codeNome = dados['code_nomeCompleto']
            paciente = Paciente.objects.filter(nomeCompleto=nomeCompleto, code_nomeCompleto=codeNome)
            paciente.update(nomeCompleto=nomeCompleto + "(OFF)"  ,visivel=False)
            return redirect('index')
        else:
            print("Erros: ", form.errors.as_data())
            return render(request, template_delete_paciente, {'form': form})

def novo_paciente(request):
    if request.method == 'GET':
        return render(request, template_novo_paciente)

    elif request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            cpf = dados['cpf']
            IMC = dados['IMC']
            sexo = dados['sexo']
            peso = dados['peso']
            altura = dados['altura']
            telefone = dados['telefone']
            observacao = dados['observacao']
            nivelAtividade = dados['nivelAtividade']
            nomeCompleto = pacienteClass.processa_string_nome(dados['nomeCompleto'])
            dataNascimento = dados['dataNascimento']

            codeNome = 0

            if Paciente.objects.filter(nomeCompleto=nomeCompleto):
                codeNome = (pacienteClass.get_maior_codeNome_paciente(nomeCompleto) + 1)

            paciente = Paciente.objects.create(cpf=cpf,
                                               IMC=IMC,
                                               sexo=sexo,
                                               peso=peso,
                                               altura=altura,
                                               telefone=telefone,
                                               observacao=observacao,
                                               nomeCompleto=nomeCompleto,
                                               code_nomeCompleto=codeNome,
                                               nivelAtividade=nivelAtividade,
                                               dataNascimento=dataNascimento,
                                               )
            paciente.save()
            avaliador = Avaliador.objects.get(user=request.user)
            avaliador.avaliador_paciente.add(paciente)
            avaliador.save()
            exame = Exame.objects.create(fk_paciente=paciente)
            exame.save()
            return redirect('index')
        else:
            print("Erros: ", form.errors.as_data())
            return render(request, template_novo_paciente, {'form': form})

def editar_paciente(request):
    if request.method == 'GET':
        context = {"pacientes": Paciente.objects.all().filter(visivel=True)}
        return render(request, template_editar_paciente, context)

    elif request.method == 'POST':
        form = EditarPacienteForm(request.POST)
        if form.is_valid(True):
            dados = form.cleaned_data
            cpf = dados['cpf']
            IMC = dados['IMC']
            sexo = dados['sexo']
            peso = dados['peso']
            altura = dados['altura']
            telefone = dados['telefone']
            observacao = dados['observacao']
            nomeCompleto = pacienteClass.processa_string_nome(dados['nomeCompleto'])
            dataNascimento = dados['dataNascimento']
            nomeCompletoCodeNome = dados['nomeCompletoCodeNome']
            dic_nomeCompleto_codeNomeCompleto_paciente = pacienteClass.get_dic_nome_codeNome(nomeCompletoCodeNome)
            nomeCompletoPaciente_anterior = dic_nomeCompleto_codeNomeCompleto_paciente['nomePaciente']
            codeNomeCompletoPaciente_anterior = dic_nomeCompleto_codeNomeCompleto_paciente['codeNomePaciente']

            codeNome = 0
            paciente = None

            if nomeCompleto in pacienteClass.get_lista_nomeCompleto_pacientes():
                codeNome = (pacienteClass.get_maior_codeNome_paciente(nomeCompleto) + 1) if nomeCompleto != nomeCompletoPaciente_anterior else codeNomeCompletoPaciente_anterior

            if nomeCompletoPaciente_anterior.isdigit():
                paciente = Paciente.objects.filter(cpf=nomeCompletoPaciente_anterior)
            else:
                paciente = Paciente.objects.filter(nomeCompleto=nomeCompletoPaciente_anterior, code_nomeCompleto=codeNomeCompletoPaciente_anterior)

            paciente.update(cpf=cpf,
                            IMC=IMC,
                            sexo=sexo,
                            peso=peso,
                            altura=altura,
                            telefone=telefone,
                            observacao=observacao,
                            nomeCompleto=nomeCompleto,
                            code_nomeCompleto=codeNome,
                            dataNascimento=dataNascimento,
                            )

            return redirect('index')

        else:
            print("Erros: ", form.errors.as_data())
            return render(request, template_editar_paciente, {'form': form})

def get_dados_paciente(request):
    dic_json = pacienteClass.get_dic_dados_paciente_search_json(request=request)
    return dic_json
