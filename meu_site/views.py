
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from .models import Noticia, PlanoInternet
from django.views.decorators.http import require_http_methods

from .models import PlanoEmpresarial


from django.shortcuts import render
from .models import Noticia


from django.http import HttpResponse

def ads_txt(request):
    content = "google.com, pub-5451545777538942, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")



def home(request):
    planos = PlanoInternet.objects.all().order_by('-destaque')
    # Prepara texto de WhatsApp por plano para uso seguro no template
    for plano in planos:
        plano.whatsapp_text = f"Quero o plano {plano.nome} ({plano.velocidade})"

    def format_whatsapp(number: str) -> str:
        if not number:
            return ''
        n = ''.join(ch for ch in number if ch.isdigit())
        # Esperado: 55 + DDD(2) + 9 + número(8)
        if len(n) >= 13 and n.startswith('55'):
            ddi = '+55'
            ddd = n[2:4]
            rest = n[4:]
            if len(rest) >= 9:
                return f"{ddi} ({ddd}) {rest[0:5]}-{rest[5:9]}"
        return number
    # Cobertura processada (ordem alfabética, flag de observação "*")
    areas_raw = getattr(settings, 'COVERAGE_AREAS', [])
    coverage = []
    for area in areas_raw:
        raw = (area or '').strip()
        is_note = raw.endswith('*')
        name_clean = raw[:-1].strip() if is_note else raw
        coverage.append({
            'name': name_clean,
            'note': is_note,
            'key': name_clean.lower(),
        })
    coverage.sort(key=lambda x: x['key'])

    context = {
        'planos': planos,
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '5599999999999'),
        'whatsapp_number_formatted': format_whatsapp(getattr(settings, 'WHATSAPP_NUMBER', '')),
        'site_name': getattr(settings, 'SITE_NAME', 'Meu Provedor'),
        'email': getattr(settings, 'SITE_EMAIL', 'contato@digitalnet.com.br'),
        'endereco': getattr(settings, 'SITE_ADDRESS', 'Informe seu endereço aqui'),
        'city_name': getattr(settings, 'CITY_NAME', ''),
        'coverage': coverage,
    }
    return render(request, 'core/home.html', context)

def home(request):
    ultimas_noticias = Noticia.objects.all().order_by('-data_publicacao')[:3]  # pega as 3 últimas
    return render(request, 'core/home.html', {'ultimas_noticias': ultimas_noticias})

# meu_site/views.py

def empresarial(request):
    planos_empresariais = PlanoEmpresarial.objects.all()
    context = {
        'site_name': 'DigitalNet',
        'planos_empresariais': planos_empresariais,
    }
    return render(request, 'core/empresarial.html', context)

def noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias.html', {'noticias': noticias})

def detalhe_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})