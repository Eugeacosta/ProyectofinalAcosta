from django.urls import include, path
from .views import SignUpView, CustomLoginView, logout_view, profile_view, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileUpdate.as_view(), name='profile_edit'),
    path('mensajeria/', include('AppMensajeria.urls')),
    
]