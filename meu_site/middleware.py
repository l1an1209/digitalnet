"""
Middleware para servir arquivos de mídia em produção
"""
import os
from django.http import Http404, HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class MediaFilesMiddleware(MiddlewareMixin):
    """
    Middleware para servir arquivos de mídia em produção
    """
    
    def process_request(self, request):
        # Verificar se a requisição é para um arquivo de mídia
        if request.path.startswith(settings.MEDIA_URL):
            # Remover o prefixo MEDIA_URL do caminho
            file_path = request.path[len(settings.MEDIA_URL):]
            
            # Construir o caminho completo do arquivo
            full_path = os.path.join(settings.MEDIA_ROOT, file_path)
            
            # Verificar se o arquivo existe
            if os.path.exists(full_path) and os.path.isfile(full_path):
                # Determinar o tipo de conteúdo
                import mimetypes
                content_type, _ = mimetypes.guess_type(full_path)
                if content_type is None:
                    content_type = 'application/octet-stream'
                
                # Ler e retornar o arquivo
                with open(full_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type=content_type)
                    response['Content-Disposition'] = f'inline; filename="{os.path.basename(full_path)}"'
                    return response
            else:
                raise Http404("Arquivo não encontrado")
        
        return None
