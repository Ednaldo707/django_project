# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # /
    path('', views.homepage, name='homepage'), 
    # /eventos/
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    # /eventos/1/
    path('eventos/<int:pk>/', views.detalhe_evento, name='detalhe_evento'),
    # Adicione rotas para Projetos, Equipes e Mídia conforme avança
]