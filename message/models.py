from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Message(models.Model):
    nombre_del_mensaje = models.CharField(max_length=40)
    message_date = models.DateTimeField(default=datetime.now)
    mensaje = models.TextField(blank = True, null=True)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f'Mensaje número: {self.id}'
