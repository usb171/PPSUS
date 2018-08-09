from django.urls import path
from .views import RegistrarTipoExameView
from . import views
urlpatterns = [
    path('novoTipoExame/', RegistrarTipoExameView.as_view(), name='novoTipoExame'),
]
