from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    # Relación con User (quien envía)
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    # Relación con User (quien recibe)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emisor} para {self.destinatario}"


