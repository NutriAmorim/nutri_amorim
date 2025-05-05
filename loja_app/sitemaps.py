# loja_app/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Produto  # Supondo que você tenha um modelo Produto
from django.urls import reverse

class ProdutoSitemap(Sitemap):
    def items(self):
        return Produto.objects.all()  # Ou outro modelo relevante

    def lastmod(self, obj):
        return obj.modified  # Modificado recentemente, ou outro campo relevante

    def location(self, obj):
        return reverse('produto_detail', args=[obj.pk])  # Ajuste conforme necessário
