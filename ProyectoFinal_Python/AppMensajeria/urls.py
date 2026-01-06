from django.urls import path
from .views import MensajeList, MensajeCreate, MensajeDetail

urlpatterns = [
    path('listar/', MensajeList.as_view(), name='mensaje_list'),
    path('crear/', MensajeCreate.as_view(), name='mensaje_create'),
    path('<int:pk>/detalle/', MensajeDetail.as_view(), name='mensaje_detail'),
]