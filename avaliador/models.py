from django.db import models
from django.contrib.auth.models import User
from paciente.models import Paciente
from dispositivo.models import Dispositivo

class Avaliador(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    dispositivo = models.OneToOneField(Dispositivo, on_delete=False, blank=True, null=True)
    avaliador_paciente = models.ManyToManyField(Paciente, blank=True)

    def __str__(self):
        return self.user.username

    def get_avaliador_paciente(self):
        return self.avaliador_paciente.all()
