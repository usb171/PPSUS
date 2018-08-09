from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from avaliador.models import Avaliador

from users.forms import RegistrarForm

class RegistrarUsuarioView(View):
    template_name = 'users/cadastro.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            usuario = User.objects.create_user(username=dados['usuario'].replace(" ", "_").lower(),
                                               email=dados['email'],
                                               password=dados['senha'])
            usuario.save()
            avaliador = Avaliador.objects.create(user=usuario)
            avaliador.save()
            # user = authenticate(username=usuario.username, password=form.cleaned_data['password'])
            # login(request, user)
            return redirect('login')
        else:
            print("Usuario: ", form['usuario'].errors)
            print("Senha:", form['senha'].errors)
            print("Email:", form['email'].errors)
            return render(request, self.template_name, {'form': form})
