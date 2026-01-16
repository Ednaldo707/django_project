from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Página Inicial
    path('', views.home, name='home'),
    
    # Novas Páginas
    path('projetos/', views.projetos, name='projetos'),
    path('midia/', views.midia, name='midia'),
    path('reserva/', views.reserva, name='reserva'),
    path('equipes/', views.equipes, name='equipes'),
    path('salvar_firebase/', views.salvar_firebase, name='salvar_firebase'), 
    path('gerenciar_projeto/<str:doc_id>/', views.gerenciar_projeto, name='gerenciar_projeto'), # <-- Linha nova adicionada
]