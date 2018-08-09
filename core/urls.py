from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('red/', views.red, name='red'),
    path('blue/', views.blue, name='blue'),
    path('green/', views.green, name='green'),
    path('tone/', views.tone, name='tone'),

    path('selecionarDispositivo/', views.selecionarDispositivo, name='selecionarDispositivo'),
    path('devolverDispositivo/', views.devolverDispositivo, name='devolverDispositivo'),


]
