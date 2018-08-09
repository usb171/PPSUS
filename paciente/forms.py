from django import forms
from paciente.models import Paciente

class EditarPacienteForm(forms.Form):
    nomeCompleto = forms.CharField(required=True)
    nomeCompletoCodeNome = forms.CharField(required=True)
    cpf = forms.CharField(required=False)
    sexo = forms.CharField(required=True)
    #nivelAtividade = forms.CharField(required=True)
    altura = forms.FloatField(required=True)
    peso = forms.FloatField(required=True)
    IMC = forms.FloatField(required=True)
    telefone = forms.CharField(required=False)
    dataNascimento = forms.DateField(required=False)
    observacao = forms.CharField(required=False)

    def is_valid_from_form(self):
        return super(EditarPacienteForm, self).is_valid()

    def is_valid(self, flag_edicao=False):

        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False

        elif not flag_edicao and Paciente.objects.filter(cpf=self.cleaned_data['cpf']).exists():
            self.add_error(field='cpf', error='CPF já cadastrado')
            return False

        elif not self.cleaned_data['sexo']:
            self.add_error(field='sexo', error='Selecione o sexo do paciente')
            return False

        return valid


class DeletarPacienteForm(forms.Form):

    nomeCompleto = forms.CharField(required=True)
    code_nomeCompleto = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(DeletarPacienteForm, self).is_valid()

    def is_valid(self, flag_edicao=False):
        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        return valid


class PacienteForm(forms.Form):

    nomeCompleto = forms.CharField(required=True)
    cpf = forms.CharField(required=False)
    sexo = forms.CharField(required=True)
    nivelAtividade = forms.CharField(required=True)
    altura = forms.FloatField(required=True)
    peso = forms.FloatField(required=True)
    IMC = forms.FloatField(required=True)
    telefone = forms.CharField(required=False)
    dataNascimento = forms.DateField(required=False)
    observacao = forms.CharField(required=False)

    def is_valid_from_form(self):
        return super(PacienteForm, self).is_valid()

    def is_valid(self, flag_edicao=False):

        valid = self.is_valid_from_form()

        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        # elif not flag_edicao and Paciente.objects.filter(nomeCompleto=self.cleaned_data['nomeCompleto'].replace(" ", "_").lower()):
        #     self.add_error(field='nomeCompleto', error='Nome já cadastrado')
        #     return False
        elif not flag_edicao and Paciente.objects.filter(visivel=True, cpf=self.cleaned_data['cpf']):
            self.add_error(field='nomeCompleto', error='CPF já cadastrado')
            return False

        elif not self.cleaned_data['nivelAtividade']:
            self.add_error(field='nivelAtividade', error='Selecione um Nível de atividade')
            return False

        elif not self.cleaned_data['sexo']:
            self.add_error(field='sexo', error='Selecione o sexo do paciente')
            return False

        return valid
