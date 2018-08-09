from django.contrib.auth import views
from django.urls import include, path
from users.views import RegistrarUsuarioView

urlpatterns = [
    path('', views.login, {'template_name': 'users/login.html'}, name='login'),
    path('', views.logout, {'next_page':'users/login.html'}, name='logout'),
    path('cadastro/', RegistrarUsuarioView.as_view(), name="cadastro"),
]