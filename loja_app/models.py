from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='pdf/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades"

class PedidoProduto(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id})'

class Endereco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', 'Digite um CEP válido com 8 dígitos.')]
    )

    def __str__(self):
        return f'{self.rua}, {self.bairro}, {self.cidade}'

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'
    
