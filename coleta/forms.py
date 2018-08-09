from django import forms
from coleta.models import Coleta
from tipoExame.models import TipoExame
from paciente.models import Paciente


# class ColetaLaudoForm(forms.Form):
#     observacao = forms.CharField(max_length=120, required=False)
#     risco_queda = forms.CharField(max_length=10, required=False)
#     cronometro = forms.CharField(max_length=10, required=False)
#     pontuacao_soma = forms.CharField(max_length=10, required=False)
#     deslocamento = forms.CharField(max_length=10, required=False)
#     pontuacao = forms.CharField(max_length=10, required=False)
#     coleta_id = forms.CharField(max_length=10, required=True)
#     def is_valid_from_form(self):
#         return super(ColetaLaudoForm, self).is_valid()
#
#     def is_valid(self, flag_edicao=False):
#         valid = self.is_valid_from_form()
#         return valid


class ColetaLaudoForm(forms.Form):
    paciente = forms.CharField(max_length=10, required=True) #Id
    tipoExame = forms.CharField(max_length=10, required=True) #Id
    observacao = forms.CharField(max_length=120, required=False)
    risco_queda = forms.CharField(max_length=10, required=False)
    cronometro = forms.CharField(max_length=10, required=False)
    pontuacao_soma = forms.CharField(max_length=10, required=False)
    deslocamento = forms.CharField(max_length=10, required=False)
    pontuacao = forms.CharField(max_length=10, required=False)
    def is_valid_from_form(self):
        return super(ColetaLaudoForm, self).is_valid()

    def is_valid(self, flag_edicao=False):
        valid = self.is_valid_from_form()
        return valid


class ColetaForm(forms.Form):

    tipoExame = forms.ModelMultipleChoiceField(queryset=TipoExame.objects.all())
    paciente = forms.ModelMultipleChoiceField(queryset=Paciente.objects.all())
    # observacao = forms.CharField(max_length=200, required=False)
    #file = forms.FileField()

    def is_valid_from_form(self):
        return super(ColetaForm, self).is_valid()

    def is_valid(self, flag_edicao=False):

        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        return valid
