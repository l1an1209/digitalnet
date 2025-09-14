
from django.shortcuts import render
from django.conf import settings
from .models import PlanoInternet
from django.views.decorators.http import require_http_methods

from .models import PlanoEmpresarial



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


# meu_site/views.py

def empresarial(request):
    planos_empresariais = PlanoEmpresarial.objects.all()
    context = {
        'site_name': 'DigitalNet',
        'planos_empresariais': planos_empresariais,
    }
    return render(request, 'core/empresarial.html', context)

