from django.urls import path
from .views import RegistrarExameView
from . import views
urlpatterns = [
    path('novoExame/', RegistrarExameView.as_view(), name='novoExame'),
    # path('novoTipoExame/', views.novoTipoExame, name='novoTipoExame'),
    path('get_dados_exame/', views.get_dados_exame, name='get_dados_exame'),
    path('editarExame/', views.editarExame, name='editarExame'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('novoExameColeta/', views.novoExameColeta, name='novoExameColeta'),
]
