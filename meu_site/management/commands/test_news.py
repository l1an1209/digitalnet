from django.core.management.base import BaseCommand
from meu_site.models import Noticia, PlanoInternet, PlanoEmpresarial
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Cria dados de exemplo para testar o site'

    def handle(self, *args, **options):
        # Criar notícias de exemplo
        noticias_data = [
            {
                'titulo': 'DigitalNet Expande Cobertura em Ji-Paraná',
                'resumo': 'Nova infraestrutura de fibra óptica chega a mais bairros da cidade, oferecendo internet de alta velocidade.',
                'conteudo': 'A DigitalNet está expandindo sua rede de fibra óptica para mais bairros de Ji-Paraná. Com investimentos em infraestrutura de última geração, a empresa promete levar internet de alta velocidade para regiões que antes não tinham acesso à tecnologia de ponta.\n\nA expansão inclui novos bairros como Jardim dos Migrantes, Nova Brasília e Parque dos Pioneiros, garantindo que mais famílias tenham acesso à internet estável e rápida.\n\n"Estamos comprometidos em democratizar o acesso à internet de qualidade em nossa cidade", afirma o diretor técnico da DigitalNet.',
                'categoria': 'Expansão'
            },
            {
                'titulo': 'Novos Planos Empresariais com Velocidades Até 1Gbps',
                'resumo': 'Empresas agora podem contratar planos dedicados com velocidades superiores para maior produtividade.',
                'conteudo': 'A DigitalNet lançou uma nova linha de planos empresariais com velocidades que chegam até 1Gbps. Os novos planos são ideais para empresas que precisam de alta performance em suas operações.\n\nCaracterísticas dos novos planos:\n- Fibra dedicada\n- Suporte técnico 24/7\n- SLA de 99,9% de disponibilidade\n- Equipamentos inclusos\n- Instalação gratuita\n\n"Com esses novos planos, as empresas podem aumentar significativamente sua produtividade e eficiência operacional", destaca o gerente comercial.',
                'categoria': 'Produtos'
            },
            {
                'titulo': 'DigitalNet Investe em Tecnologia 5G Ready',
                'resumo': 'Infraestrutura preparada para futuras tecnologias 5G, garantindo evolução contínua dos serviços.',
                'conteudo': 'A DigitalNet está preparando sua infraestrutura para as futuras tecnologias 5G. Com investimentos em equipamentos de última geração, a empresa garante que seus clientes terão acesso às mais modernas tecnologias de conectividade.\n\nA preparação inclui:\n- Atualização de equipamentos de rede\n- Capacitação da equipe técnica\n- Testes de compatibilidade\n- Planejamento de expansão\n\n"Estamos sempre um passo à frente, preparando o futuro da conectividade em Ji-Paraná", afirma o CEO da empresa.',
                'categoria': 'Tecnologia'
            }
        ]

        for noticia_data in noticias_data:
            slug = slugify(noticia_data['titulo'])
            noticia, created = Noticia.objects.get_or_create(
                slug=slug,
                defaults=noticia_data
            )
            if created:
                self.stdout.write(f'Notícia criada: {noticia.titulo}')
            else:
                self.stdout.write(f'Notícia já existe: {noticia.titulo}')

        # Criar planos residenciais de exemplo
        planos_residenciais = [
            {
                'nome': 'Básico',
                'velocidade': '100',
                'preco': 49.90,
                'descricao': 'Ideal para uso doméstico básico',
                'destaque': False
            },
            {
                'nome': 'Família',
                'velocidade': '300',
                'preco': 79.90,
                'descricao': 'Perfeito para famílias com múltiplos dispositivos',
                'destaque': True
            },
            {
                'nome': 'Premium',
                'velocidade': '600',
                'preco': 119.90,
                'descricao': 'Para usuários que precisam de máxima velocidade',
                'destaque': False
            }
        ]

        for plano_data in planos_residenciais:
            plano, created = PlanoInternet.objects.get_or_create(
                nome=plano_data['nome'],
                defaults=plano_data
            )
            if created:
                self.stdout.write(f'Plano residencial criado: {plano.nome}')
            else:
                self.stdout.write(f'Plano residencial já existe: {plano.nome}')

        # Criar planos empresariais de exemplo
        planos_empresariais = [
            {
                'nome': 'Empresarial 500',
                'velocidade': '500',
                'preco': 299.90,
                'descricao': 'Ideal para pequenas empresas',
                'destaque': False,
                'whatsapp_text': 'Olá! Quero contratar o plano Empresarial 500.'
            },
            {
                'nome': 'Empresarial 1G',
                'velocidade': '1000',
                'preco': 599.90,
                'descricao': 'Para empresas que precisam de máxima performance',
                'destaque': True,
                'whatsapp_text': 'Olá! Quero contratar o plano Empresarial 1G.'
            }
        ]

        for plano_data in planos_empresariais:
            plano, created = PlanoEmpresarial.objects.get_or_create(
                nome=plano_data['nome'],
                defaults=plano_data
            )
            if created:
                self.stdout.write(f'Plano empresarial criado: {plano.nome}')
            else:
                self.stdout.write(f'Plano empresarial já existe: {plano.nome}')

        self.stdout.write(
            self.style.SUCCESS('Dados de exemplo criados com sucesso!')
        )
