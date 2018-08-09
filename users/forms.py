from django import forms
from django.contrib.auth.models import User

class RegistrarForm(forms.Form):
    usuario = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    senha_confirma = forms.CharField(required=True)
    email = forms.EmailField(required=True)



    def is_valid_from_form(self):
        return super(RegistrarForm, self).is_valid()

    def is_valid(self):

        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        elif User.objects.filter(username=self.cleaned_data['usuario']).exists():
            self.add_error(field='usuario', error='Usuário já cadastrado')
            return False
        elif User.objects.filter(email=self.cleaned_data['email']).exists():
            self.add_error(field='usuario', error='Email já cadastrado')
            return False
        elif self.cleaned_data['senha'] != self.cleaned_data['senha_confirma']:
            self.add_error(field='senha', error='Senhas não correspondem')
            return False
        return valid