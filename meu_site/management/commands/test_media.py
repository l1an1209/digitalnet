from django.core.management.base import BaseCommand
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Testa se os arquivos de mídia estão sendo servidos corretamente'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        media_url = settings.MEDIA_URL
        
        self.stdout.write(f"MEDIA_ROOT: {media_root}")
        self.stdout.write(f"MEDIA_URL: {media_url}")
        
        # Verificar se a pasta existe
        if os.path.exists(media_root):
            self.stdout.write(f"✅ Pasta de mídia existe: {media_root}")
            
            # Listar arquivos na pasta de notícias
            noticias_path = os.path.join(media_root, 'noticias')
            if os.path.exists(noticias_path):
                files = os.listdir(noticias_path)
                self.stdout.write(f"📁 Arquivos em noticias/: {files}")
                
                for file in files:
                    if not file.startswith('.'):
                        file_path = os.path.join(noticias_path, file)
                        file_url = f"{media_url}noticias/{file}"
                        self.stdout.write(f"🔗 URL do arquivo: {file_url}")
                        self.stdout.write(f"📄 Caminho completo: {file_path}")
                        self.stdout.write(f"✅ Arquivo existe: {os.path.exists(file_path)}")
            else:
                self.stdout.write("❌ Pasta noticias/ não existe")
        else:
            self.stdout.write(f"❌ Pasta de mídia não existe: {media_root}")
            self.stdout.write("Criando pasta de mídia...")
            os.makedirs(media_root, exist_ok=True)
            os.makedirs(os.path.join(media_root, 'noticias'), exist_ok=True)
            self.stdout.write("✅ Pasta de mídia criada!")
