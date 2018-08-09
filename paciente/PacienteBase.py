from .models import Paciente
from avaliador.models import Avaliador
from django.http import JsonResponse

class PacienteClass():

    # Busca todos os pacientes de um avaliador(Usuário)
    def listar_paciente_avaliador(self, user):
        context = {}
        pacientes_do_avaliador = Avaliador.objects.get(user=user).avaliador_paciente.filter(visivel=True)
        lista_pacientes_avaliador = []
        for p_a in pacientes_do_avaliador: lista_pacientes_avaliador.append(p_a)
        return lista_pacientes_avaliador

    #Processa a string do nome do paciente, extraindo o nome seu códido em forma de dicionário
    def get_dic_nome_codeNome(self, nomePacienteCodeNomePaciente):
        pos_string = nomePacienteCodeNomePaciente.find("(")
        if pos_string != -1:
            nome_paciente_search = nomePacienteCodeNomePaciente[:pos_string]
            code_nome_paciente_search = nomePacienteCodeNomePaciente[pos_string:]
            string_not = ['(',')']
            for i in range(0,len(string_not)): code_nome_paciente_search = code_nome_paciente_search.replace(string_not[i],"")
            return { "nomePaciente": nome_paciente_search, "codeNomePaciente":code_nome_paciente_search}
        else:
            return { "nomePaciente": nomePacienteCodeNomePaciente, "codeNomePaciente":0}

    #Troca espaço por anderline
    def processa_string_nome(self, nome):
        return nome.replace(" ", "_").lower()

    # Retorna uma lista contendo todos os nomes de todos os pacientes do banco
    def get_lista_nomeCompleto_pacientes(self):
        return list(map(lambda x: x.nomeCompleto ,Paciente.objects.all()))

    # Retorna o miaor codeName de do paciente com nomeCompleto
    def get_maior_codeNome_paciente(self, nomeCompleto):
        lista = list(map(lambda x: x.code_nomeCompleto, Paciente.objects.filter(nomeCompleto=self.processa_string_nome(nomeCompleto))))
        if lista: return int(max(lista))
        else: return 0

    def get_dic_dados_paciente_search_json(self, request):
        paciente_search = request.GET.get('paciente_search', None)
        paciente = None
        if paciente_search.isdigit():
            paciente = Paciente.objects.get(cpf=paciente_search, visivel=True)
        else:
            dic_filtro = self.get_dic_nome_codeNome(paciente_search)
            paciente = Paciente.objects.get(nomeCompleto=dic_filtro["nomePaciente"], code_nomeCompleto=dic_filtro["codeNomePaciente"])

        nomeCompleto = paciente.nomeCompleto.replace("_"," ")
        code_NomeCompleto = paciente.code_nomeCompleto
        sexo = paciente.sexo
        peso = paciente.peso
        altura = paciente.altura
        imc = paciente.IMC
        telefone = paciente.telefone
        dataNascimento = paciente.dataNascimento
        observacao = paciente.observacao
        cpf = paciente.cpf
        id = paciente.id
        data = {
            'id': id,
            'cpf': cpf,
            'IMC': imc,
            'sexo': sexo,
            'peso': peso,
            'altura': altura,
            'telefone': telefone,
            'observacao': observacao,
            'nomeCompleto': nomeCompleto,
            'dataNascimento': dataNascimento,
            'code_nomeCompleto':code_NomeCompleto,
        }
        return JsonResponse(data)
