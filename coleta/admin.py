from django.contrib import admin
from .models import Coleta

class RegistrarColetaView(admin.ModelAdmin):
    list_display = ( 'paciente', 'tipoExame')

admin.site.register(Coleta)
