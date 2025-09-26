from django.core.management.base import BaseCommand
from meu_site.models import Noticia, PlanoInternet, PlanoEmpresarial

class Command(BaseCommand):
    help = 'Limpa todos os dados de exemplo'

    def handle(self, *args, **options):
        # Limpar todos os dados
        Noticia.objects.all().delete()
        PlanoInternet.objects.all().delete()
        PlanoEmpresarial.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Todos os dados foram limpos!')
        )
