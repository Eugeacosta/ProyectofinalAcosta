from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relación 1 a 1: Un usuario tiene un perfil, un perfil es de un usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campos extra
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


