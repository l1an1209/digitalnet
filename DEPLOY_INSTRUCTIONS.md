# 🚀 Instruções de Deploy para o Render

## ✅ Problemas Corrigidos

1. **Pillow (PIL) adicionado ao requirements.txt**
2. **Admin das notícias corrigido (removido allow_tags depreciado)**
3. **Configurações de mídia otimizadas para produção**

## 📋 Passos para Deploy no Render

### 1. Configurações no Render Dashboard

1. **Build Command:**
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```

2. **Start Command:**
   ```bash
   gunicorn provedor.wsgi:application
   ```

3. **Environment Variables:**
   - `DEBUG`: `False`
   - `SECRET_KEY`: (gerar automaticamente)
   - `DATABASE_URL`: (conectar com PostgreSQL do Render)

### 2. Configurações de Banco de Dados

- Use PostgreSQL no Render
- Configure a variável `DATABASE_URL` automaticamente
- O Django já está configurado para usar `dj_database_url`

### 3. Arquivos Estáticos

- Os arquivos estáticos serão coletados automaticamente
- O WhiteNoise está configurado para servir arquivos estáticos

### 4. Arquivos de Mídia (Imagens)

- As imagens das notícias serão salvas em `media/noticias/`
- Em produção, considere usar AWS S3 para arquivos de mídia
- Por enquanto, funcionará com o sistema de arquivos local

## 🔧 Arquivos Modificados

1. **requirements.txt** - Adicionado Pillow>=10.0.0
2. **admin.py** - Removido allow_tags depreciado
3. **settings.py** - Configurações de mídia otimizadas
4. **render.yaml** - Configuração automática do Render

## 🧪 Teste Local

Para testar localmente:

```bash
cd digitalnet-master
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/admin/`

## 📱 Funcionalidades

- ✅ Notícias com upload de imagens
- ✅ Planos residenciais e empresariais
- ✅ Admin profissional
- ✅ Design responsivo moderno
- ✅ Integração WhatsApp

## 🚨 Notas Importantes

1. **Imagens em Produção:** Para melhor performance, considere usar AWS S3
2. **Backup:** Configure backup automático do banco de dados
3. **Monitoramento:** Use os logs do Render para monitorar erros
4. **SSL:** O Render fornece SSL automático

## 🎯 Próximos Passos

1. Fazer commit das alterações
2. Fazer push para o GitHub
3. Conectar o repositório no Render
4. Configurar as variáveis de ambiente
5. Fazer deploy
6. Testar upload de imagens no admin
