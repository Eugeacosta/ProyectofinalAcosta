from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

# Vista de Registro (Sign Up)
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Al registrarse, va al login
    template_name = 'accounts/signup.html'

# Vista de Login (Personalizada para usar nuestro template)
class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/login.html'

# Vista de Logout (Manual para evitar problemas de versiones nuevas de Django)
def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required # Solo usuarios logueados pueden ver esto
def profile_view(request):
    # Busca el perfil del usuario actual. Si no existe, lo crea.
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    return render(request, 'accounts/profile.html', {'profile': profile})

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar', 'biografia', 'link'] # Campos que permitimos editar
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile') # Al guardar, vuelve al perfil

    # Este método asegura que solo edites TU propio perfil
    def get_object(self):
        # Recupera el perfil del usuario logueado
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


