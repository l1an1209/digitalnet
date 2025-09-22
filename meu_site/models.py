
from django.db import models

class PlanoInternet(models.Model):
    nome = models.CharField(max_length=100)
    velocidade = models.CharField(max_length=50)  # Ex: "300 Mega"
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class BusinessLead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    contact_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='novo')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Lead Empresarial'
        verbose_name_plural = 'Leads Empresariais'

    def __str__(self):
        return f"{self.company_name} ({self.contact_name})"


# meu_site/models.py
class PlanoEmpresarial(models.Model):
    nome = models.CharField(max_length=100)
    velocidade = models.CharField(max_length=50)  # Ex: "500 Mega"
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    destaque = models.BooleanField(default=False)
    whatsapp_text = models.CharField(max_length=255, default="Olá! Quero contratar este plano.")

    def __str__(self):
        return self.nome


# models.py
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo