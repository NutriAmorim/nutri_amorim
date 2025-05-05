from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap  # Importando a view do sitemap
from loja_app.sitemaps import ProdutoSitemap  # Importando o sitemap do seu app

# Definindo quais sitemaps serão usados
sitemaps = {
    'produtos': ProdutoSitemap,  # Nome do sitemap e a classe correspondente
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', include('loja_app.urls')),
    # Configuração do Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
