# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresarial/', views.empresarial, name='empresarial'),
    path('noticias/', views.noticias, name='noticias'),
    path("ads.txt", views.ads_txt, name="ads_txt"),
    path('noticia/<slug:slug>/', views.detalhe_noticia, name='noticia_detalhe'),
]
