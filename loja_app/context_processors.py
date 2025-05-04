from .models import Carrinho

def carrinho_total(request):
    if request.user.is_authenticated:
        total_itens = Carrinho.objects.filter(usuario=request.user).count()
    else:
        total_itens = 0
    return {'total_itens_carrinho': total_itens}
