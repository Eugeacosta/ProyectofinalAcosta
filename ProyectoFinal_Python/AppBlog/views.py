from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy # Necesario para redirigir después de borrar
from django.views.generic import CreateView, UpdateView, DeleteView # Pasos clave para CBV
from django.contrib.auth.mixins import LoginRequiredMixin # Para obligar a estar logueado
from .models import Post
def inicio(request):
    return render(request, "AppBlog/inicio.html") # Vista para la página de inicio del blog

def about(request):
    return render(request, "AppBlog/about.html") # Vista para la página "About" del blog

def post_list(request):
    posts = Post.objects.all()  # Obtener todos los posts del modelo Post
    return render(request, "AppBlog/post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "AppBlog/post_detail.html", {"post": post}) # Vista para el detalle de un post específico

# --- VISTAS BASADAS EN CLASES (CBV) ---

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen'] # Qué campos mostrar
    success_url = reverse_lazy('post_list') # A dónde ir tras crear
    
    # asignar automáticamente el autor como el usuario logueado
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('post_list')
   

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    