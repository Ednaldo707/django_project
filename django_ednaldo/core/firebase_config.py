import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings
import os

# Inicializa Firebase apenas uma vez
if not firebase_admin._apps:
    cred_path = settings.FIREBASE_CREDENTIALS_PATH
    
    if os.path.exists(cred_path):
        cred = credentials.Certificate(str(cred_path))
        firebase_admin.initialize_app(cred)
        print("✅ Firebase inicializado com sucesso!")
    else:
        print("⚠️  ATENÇÃO: Arquivo firebase_credentials.json não encontrado!")
        print(f"   Coloque o arquivo em: {cred_path}")

# Cliente Firestore
db = firestore.client()

# Funções auxiliares para Firestore
def get_collection(collection_name):
    """Retorna uma coleção do Firestore"""
    return db.collection(collection_name)

def get_document(collection_name, doc_id):
    """Retorna um documento específico"""
    doc = db.collection(collection_name).document(doc_id).get()
    if doc.exists:
        return doc.to_dict()
    return None

def get_all_documents(collection_name):
    """Retorna todos os documentos de uma coleção"""
    docs = db.collection(collection_name).stream()
    return [{'id': doc.id, **doc.to_dict()} for doc in docs]

def add_document(collection_name, data):
    """Adiciona um novo documento"""
    doc_ref = db.collection(collection_name).add(data)
    return doc_ref[1].id

def delete_document(collection_name, doc_id):
    """Remove um documento se ele existir e retorna True, senão False"""
    doc_ref = db.collection(collection_name).document(doc_id)
    if doc_ref.get().exists:
        doc_ref.delete()
        return True
    return False

def update_document(collection_name, doc_id, data):
    """Atualiza um documento se ele existir e retorna True, senão False"""
    doc_ref = db.collection(collection_name).document(doc_id)
    if doc_ref.get().exists:
        doc_ref.update(data)
        return True
    return False