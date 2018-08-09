from django import forms
from coleta.models import Coleta
from paciente.models import Paciente
from tipoExame.models import TipoExame

class TipoExameForm(forms.Form):
    nomeExame = forms.CharField(max_length=20)

    def is_valid_from_form(self):
        return super(TipoExameForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not valid:
            print("Entrei aqui")
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        elif TipoExame.objects.filter(nomeExame=self.cleaned_data['nomeExame'].replace(" ", "_").lower()).exists():
            self.add_error(field='nomeExame', error='Tipo de exame já cadastrado')
            return False
        return valid
