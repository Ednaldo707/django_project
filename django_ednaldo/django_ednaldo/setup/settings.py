import os
from pathlib import Path

# BASE_DIR aponta para a raiz do projeto (onde está o manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jizsl0nhu+&08-b-_!7-g)gzrx@-(efu(j3wcg413t4hsul_wb'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Seu app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- CORREÇÃO AQUI ---
# O Django estava procurando 'manager_maker.urls', mas sua pasta é 'setup'
ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Garante que o Django ache sua pasta de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- CORREÇÃO AQUI ---
WSGI_APPLICATION = 'setup.wsgi.application'

# Como você quer usar APENAS o Firebase, deixamos o SQLite vazio ou comentado
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- CONFIGURAÇÃO DE ARQUIVOS ESTÁTICOS (CSS) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURAÇÃO FIREBASE ---
# Certifique-se de que o arquivo .json tem este nome exato na raiz do projeto
FIREBASE_CREDENTIALS_PATH = BASE_DIR / 'projeto-maila-selles-firebase-adminsdk-fbsvc-b0e912349c.json'