# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresarial/', views.empresarial, name='empresarial'),
]
