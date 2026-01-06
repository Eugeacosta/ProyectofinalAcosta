from django.urls import path
from .views import inicio, about, post_list, post_detail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'), 
    path('pages/', post_list, name='post_list'),
    path('pages/<int:post_id>/', post_detail, name='post_detail'),
    path('pages/crear/', PostCreate.as_view(), name='post_create'),
    path('pages/<int:pk>/editar/', PostUpdate.as_view(), name='post_update'),
    path('pages/<int:pk>/borrar/', PostDelete.as_view(), name='post_delete'),
]
