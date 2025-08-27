
from django.shortcuts import render
from django.conf import settings
from .models import PlanoInternet, BusinessLead
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse

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


@require_http_methods(["GET", "POST"])
def empresarial(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name', '').strip()
        cnpj = request.POST.get('cnpj', '').strip()
        contact_name = request.POST.get('contact_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        if company_name and cnpj and contact_name and phone:
            BusinessLead.objects.create(
                company_name=company_name,
                cnpj=cnpj,
                contact_name=contact_name,
                email=email or 'sem-email@local',
                phone=phone,
                message=message,
            )
            return HttpResponseRedirect(reverse('empresarial') + '?ok=1')

    context = {
        'site_name': getattr(settings, 'SITE_NAME', 'Meu Provedor'),
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '5599999999999'),
    }
    return render(request, 'core/empresarial.html', context)
