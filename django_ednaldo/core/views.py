# core/views.py

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Evento

def homepage(request):
    """View para a Home/Dashboard com os 4 botões de navegação."""
    context = {
        'titulo': 'LabMarker - Início',
        # Aqui você pode adicionar contagens ou dados da dashboard se necessário
    }
    return render(request, 'core/home.html', context)

def lista_eventos(request):
    """View para listar eventos futuros."""
    # Filtra apenas eventos cuja data seja maior ou igual à data de hoje
    eventos_futuros = Evento.objects.filter(data__gte=timezone.now().date()).order_by('data', 'horario')
    
    context = {
        'titulo': 'Próximos Eventos',
        'eventos': eventos_futuros,
    }
    return render(request, 'core/eventos.html', context)

def detalhe_evento(request, pk):
    """View para mostrar os detalhes de um evento específico."""
    evento = get_object_or_404(Evento, pk=pk)
    
    context = {
        'titulo': f'Evento: {evento.titulo}',
        'evento': evento,
    }
    return render(request, 'core/detalhe_evento.html', context)