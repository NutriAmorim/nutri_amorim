from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Utilize os nomes das rotas exatamente como definidos no arquivo urls.py
        return [
            'home',             # Página inicial
            'login',            # Página de login
            'cadastro',         # Página de cadastro
            'painel',           # Página de painel
            'logout',           # Página de logout
            'plataforma',       # Página de plataforma
        ]

    def location(self, item):
        try:
            return reverse(item)
        except Exception as e:
            print(f"Erro ao reverter a URL para o item '{item}': {e}")
            return '/'
