# core/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .firebase_config import get_all_documents, add_document 


def home(request):
    return render(request, 'core/home.html')

def projetos(request):
    """Página de Projetos dinâmica carregando dados do Firebase"""
    # 1. Busca os dados nas coleções do Firebase
    lista_projetos = get_all_documents('projetos')
    lista_exposicoes = get_all_documents('exposicoes')
    
    # 2. Lógica para as estatísticas (Cards do topo)
    # Filtramos quantos estão em andamento e quantos estão concluídos
    projetos_andamento = [p for p in lista_projetos if p.get('status') == 'andamento']
    projetos_concluidos = [p for p in lista_projetos if p.get('status') == 'concluido']
    
    stats = {
        'total_andamento': len(projetos_andamento),
        'total_concluidos': len(projetos_concluidos),
        'total_pontos': len(lista_exposicoes)
    }

    # 3. Organiza o contexto para o HTML
    context = {
        'projetos': lista_projetos,
        'exposicoes': lista_exposicoes,
        'stats': stats
    }
    
    return render(request, 'core/projetos.html', context)

def midia(request):
    return render(request, 'core/midia.html')

def reserva(request):
    return render(request, 'core/reserva.html')

def equipes(request):
    return render(request, 'core/equipes.html')

@csrf_exempt
def salvar_firebase(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        colecao = dados.pop('colecao') # Remove 'colecao' dos dados e guarda na variável
        
        # Usa sua função já existente do firebase_config.py
        add_document(colecao, dados) 
        
        return JsonResponse({'status': 'sucesso'})
    return JsonResponse({'status': 'erro'}, status=400)


@csrf_exempt
def gerenciar_projeto(request, doc_id):
    from .firebase_config import delete_document, update_document
    colecoes = ['projetos', 'exposicoes'] # As coleções onde o sistema vai buscar o ID

    if request.method == 'DELETE':
        for colecao in colecoes:
            # Tentamos deletar. Se a função delete_document retornar True, paramos.
            if delete_document(colecao, doc_id):
                return JsonResponse({'status': 'sucesso', 'mensagem': f'Removido de {colecao}'})
        return JsonResponse({'status': 'erro', 'message': 'ID não encontrado'}, status=404)
    
    if request.method == 'POST':
        dados = json.loads(request.body)
        for colecao in colecoes:
            # Tentamos atualizar. Se a função update_document retornar True, paramos.
            if update_document(colecao, doc_id, dados):
                return JsonResponse({'status': 'sucesso', 'mensagem': f'Atualizado em {colecao}'})
        return JsonResponse({'status': 'erro', 'message': 'ID não encontrado'}, status=404)

    return JsonResponse({'status': 'erro'}, status=400)