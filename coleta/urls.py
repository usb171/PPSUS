from django.urls import path
from . import views
urlpatterns = [
    path('novaFicha/', views.novaFicha, name='novaFicha'),
    path('novaColeta/', views.novaColeta, name='novaColeta'),
    path('salvarLaudo/', views.salvarLaudo, name='salvarLaudo'),
    path('coletarDados/', views.coletarDados, name='coletarDados'),
    path('get_dados_paciente/', views.get_dados_paciente, name='get_dados_paciente'),
    path('get_dados_tipo_exame/', views.get_dados_tipo_exame, name='get_dados_tipo_exame'),
    path('iniciarColeta/', views.iniciarColeta, name='iniciarColeta'),
    path('finalizarColeta/', views.finalizarColeta, name='finalizarColeta'),
    path('cancelarColeta/', views.cancelarColeta, name='cancelarColeta'),

]
