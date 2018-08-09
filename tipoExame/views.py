from django.shortcuts import render, redirect
from django.views import View
from tipoExame.forms import TipoExameForm
from tipoExame.models import TipoExame

class RegistrarTipoExameView(View):

    def get(self, request):
        return render(request, "tipoExame/novoTipoExame.html")

    def post(self, request):
        form = TipoExameForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            tipo_exame = TipoExame.objects.create(nomeExame=dados['nomeExame'].replace(" ", "_").lower())
            tipo_exame.save()
            return redirect('index')
        else:
            print("Erros: ", form.errors.as_data())
            return render(request, "tipoExame/novoTipoExame.html", {'form': form})
