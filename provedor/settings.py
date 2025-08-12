# provedor/settings.py
from pathlib import Path
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-)rg(360-i)eg_3^*m!8wy7m&ev)rzp0+8@f+)*wjphqj5$#577')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meu_site',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Adicionado para servir arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'provedor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'provedor.wsgi.application'

# Configuração do banco de dados para Render
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Admin branding
from django.utils.translation import gettext_lazy as _
ADMIN_SITE_HEADER = _('DigitalNet — Administração')
ADMIN_SITE_TITLE = _('DigitalNet Admin')
ADMIN_INDEX_TITLE = _('Painel de Controle')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom project settings
WHATSAPP_NUMBER = '5569992820543'
SITE_NAME = 'DigitalNet'
SITE_EMAIL = 'contato@digitalnet.com.br'
SITE_ADDRESS = 'Sua rua, número, bairro — Cidade/UF'
CITY_NAME = 'Ji-Paraná'
COVERAGE_AREAS = [
    'Açai', 'Copas Verdes', 'Jardim das Seringueiras', 'Parque dos Pioneiros', 'BNH',
    'Distrito Industrial', 'Jardim dos Migrantes', 'Parque São Pedro', 'Bosque dos Ipês',
    'Dois de Abril', 'Nova Brasilia', 'Santiago', 'Cafezinho', 'Dom Bosco', 'Novo Horizonte',
    'São Bernado', 'Capelasso', 'Estrada do Aeroporto', 'Novo Ji-Paraná', 'São Cristovão',
    'Casa Preta*', 'Green park', 'Novo Urupá', 'União (Beira-Rio)', 'Centro', 'Greenvile',
    'Orleans II', 'União II', 'Cidade Jardim', 'Habitar Brasil', 'Parque Amazonas',
    'Vila de Rondônia', 'Colina Park I e II', 'Jardim Aurelio Bernadi', 'Parque Brasil',
    'Zona Rural*', 'Planalto I e II', 'Jardim Presidencial I e II',
]
