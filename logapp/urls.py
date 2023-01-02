import os
from django.urls import path
from regapp.settings import BASE_DIR, MEDIA_URL
from .views import Logout_views, certificate, register, home, create_post
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='Home'),
    path('login/', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('logout/', Logout_views, name='logout'),
    path('register/', register, name='register'),
    path('create/', create_post, name='create'),
    path('certificate/', certificate, name='certificate')
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)