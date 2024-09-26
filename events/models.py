from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)  # Nombre del evento
    description = models.TextField()  # Descripción del evento
    place = models.CharField(max_length=200)  # Lugar del evento
    date = models.DateTimeField()  # Fecha y hora del evento
    date_creation = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que creó el evento
    activated_notification = models.BooleanField(default=False)  # Notificación activada

    def __str__(self):
        return self.name