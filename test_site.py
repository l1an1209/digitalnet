#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'provedor.settings')
django.setup()

from meu_site.models import Noticia, PlanoInternet, PlanoEmpresarial
from django.utils.text import slugify

def clear_data():
    """Limpa todos os dados existentes"""
    print("Limpando dados existentes...")
    Noticia.objects.all().delete()
    PlanoInternet.objects.all().delete()
    PlanoEmpresarial.objects.all().delete()
    print("✅ Dados limpos!")

def create_sample_data():
    """Cria dados de exemplo"""
    print("Criando dados de exemplo...")
    
    # Criar notícias
    noticias_data = [
        {
            'titulo': 'DigitalNet Expande Cobertura',
            'slug': 'digitalnet-expande-cobertura',
            'resumo': 'Nova infraestrutura de fibra óptica chega a mais bairros.',
            'conteudo': 'A DigitalNet está expandindo sua rede de fibra óptica para mais bairros de Ji-Paraná.',
            'categoria': 'Expansão'
        },
        {
            'titulo': 'Novos Planos Empresariais',
            'slug': 'novos-planos-empresariais',
            'resumo': 'Empresas agora podem contratar planos dedicados.',
            'conteudo': 'A DigitalNet lançou uma nova linha de planos empresariais.',
            'categoria': 'Produtos'
        }
    ]
    
    for data in noticias_data:
        noticia, created = Noticia.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if created:
            print(f"✅ Notícia criada: {noticia.titulo}")
        else:
            print(f"ℹ️ Notícia já existe: {noticia.titulo}")
    
    # Criar planos residenciais
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
            'descricao': 'Perfeito para famílias',
            'destaque': True
        }
    ]
    
    for data in planos_residenciais:
        plano, created = PlanoInternet.objects.get_or_create(
            nome=data['nome'],
            defaults=data
        )
        if created:
            print(f"✅ Plano residencial criado: {plano.nome}")
        else:
            print(f"ℹ️ Plano residencial já existe: {plano.nome}")
    
    # Criar planos empresariais
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
    
    for data in planos_empresariais:
        plano, created = PlanoEmpresarial.objects.get_or_create(
            nome=data['nome'],
            defaults=data
        )
        if created:
            print(f"✅ Plano empresarial criado: {plano.nome}")
        else:
            print(f"ℹ️ Plano empresarial já existe: {plano.nome}")
    
    print("\n🎉 Dados de exemplo criados com sucesso!")
    print(f"📰 Notícias: {Noticia.objects.count()}")
    print(f"🏠 Planos residenciais: {PlanoInternet.objects.count()}")
    print(f"🏢 Planos empresariais: {PlanoEmpresarial.objects.count()}")

if __name__ == '__main__':
    try:
        clear_data()
        create_sample_data()
    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)
