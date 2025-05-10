from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'home',                    # Página inicial do app principal
            'usuarios:login',          # Página de login (namespace: usuarios)
            'usuarios:logout',         # Página de logout (namespace: usuarios)
            'sobre_mim',               # Página "Sobre Mim"
            'conheca_nosso_trabalho',   # Página "Conheça Nosso Trabalho"
        ]

    def location(self, item):
        return reverse(item)