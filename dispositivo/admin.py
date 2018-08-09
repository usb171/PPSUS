from django.contrib import admin
from .models import Dispositivo

class DispositivoView(admin.ModelAdmin):
    list_display = ( 'nome', 'codigo')

admin.site.register(Dispositivo)
