from django.contrib import admin
from .models import Produto, Carrinho
from .models import AvaliacaoNutricional

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'arquivo')  # Mostra essas colunas na listagem
    search_fields = ('nome',)  # Adiciona uma barra de pesquisa por nome

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'usuario', 'data_adicionado')
    list_filter = ('usuario',)  # Filtro lateral por usuário
    search_fields = ('produto__nome',)  # Barra de pesquisa por nome do produto

@admin.register(AvaliacaoNutricional)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'peso_atual', 'altura', 'atividade_fisica', 'data_envio')
    list_filter = ('sexo', 'atividade_fisica')
    search_fields = ('nome', 'contato')