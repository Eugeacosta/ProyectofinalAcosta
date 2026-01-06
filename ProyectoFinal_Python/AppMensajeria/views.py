from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Mensaje
from django.contrib.auth.models import User

# 1. Crear Mensaje (Escribir)
class MensajeCreate(LoginRequiredMixin, CreateView):
    model = Mensaje
    fields = ['destinatario', 'cuerpo'] # El usuario elige a quién y qué escribir
    success_url = reverse_lazy('mensaje_list') # Al enviar, vuelve al buzón
    template_name = 'AppMensajeria/mensaje_form.html'

    # Truco: Asignamos automáticamente el emisor como el usuario logueado
    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)

# 2. Listar Mensajes (Buzón de Entrada)
class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'AppMensajeria/mensaje_list.html'
    context_object_name = 'mensajes'

    # Filtramos para mostrar SOLO los mensajes que recibió el usuario logueado
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user).order_by('-fecha_envio')

# 3. Leer Mensaje Completo (Detalle)
class MensajeDetail(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'AppMensajeria/mensaje_detail.html'


