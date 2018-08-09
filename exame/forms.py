from django import forms
from .models import Exame #,TipoExame
from paciente.models import Paciente


# class TipoExameForms(forms.Form):
#     nomeExame = forms.CharField(max_length=20)
#
#     def is_valid_from_form(self):
#         return super(TipoExameForms, self).is_valid()
#
#     def is_valid(self):
#         valid = self.is_valid_from_form()
#         if not valid:
#             print("Entrei aqui")
#             self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
#             return False
#         elif TipoExame.objects.filter(nomeExame=self.cleaned_data['nomeExame'].replace(" ", "_").lower()).exists():
#             self.add_error(field='nomeExame', error='Tipo de exame já cadastrado')
#             return False
#         return valid

class ExameForm(forms.Form):

    #fk_tipoExame = forms.ModelChoiceField(queryset=TipoExame.objects.all())
    fk_paciente = forms.ModelMultipleChoiceField(queryset=Paciente.objects.all())
    # observacao = forms.CharField(max_length=200)
    #file = forms.FileField()

    def is_valid_from_form(self):
        return super(ExameForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        return valid

    class Meta:
        model = Exame
        fields = "__all__"


# class ExameForm(forms.Form):
#     fk_paciente = forms.ModelMultipleChoiceField(queryset=Paciente.objects.all())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         fk_paciente = cleaned_data.get("fk_paciente")
#
#         if not fk_paciente:
#             msg = "Nada"
#             self.add_error('fk_paciente', msg)
