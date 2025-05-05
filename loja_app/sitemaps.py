from django.contrib.sitemaps import Sitemap
from .models import Produto

class ProdutoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Produto.objects.all()

    def location(self, obj):
        return f"/produto/{obj.slug}/"
