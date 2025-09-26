"""
Configuração para servir arquivos de mídia em produção
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meu_site.urls')),
]

# Servir arquivos de mídia em produção
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Em produção, você pode usar um serviço como AWS S3
    # Por enquanto, vamos servir localmente
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
