from django.urls import path
from . import views
urlpatterns = [
    path('novoPaciente/', views.novo_paciente, name='novoPaciente'),
    path('editarPaciente/', views.editar_paciente, name='editarPaciente'),
    path('deletarPaciente/', views.deletar_paciente, name='deletarPaciente'),
    path('get_dados_paciente/', views.get_dados_paciente, name='get_dados_paciente'),
]
