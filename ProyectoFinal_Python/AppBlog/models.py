from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model): # Modelo para las entradas del blog
    titulo = models.CharField(max_length=200) # Título del post
    subtitulo = models.CharField(max_length=200) # Subtítulo del post
    cuerpo = RichTextField(blank=True, null=True) # Campo de texto enriquecido
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # Relación con el modelo User
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True) # Fecha de publicación automática

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
