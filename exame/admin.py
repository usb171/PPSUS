from django.contrib import admin

from .models import Exame
# from .forms import ExameForm
from tipoExame.models import TipoExame

class ExameAdmin(admin.ModelAdmin):
    list_display = ( 'fk_paciente', 'id')



admin.site.register(Exame, ExameAdmin)

#admin.site.register(Exame)
admin.site.register(TipoExame)
