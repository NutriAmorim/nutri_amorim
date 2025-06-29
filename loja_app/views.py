from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrinho, Pedido, PedidoProduto
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from babel.numbers import format_currency
from .models import Produto
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nltk.chat.util import Chat, reflections
import json
import unicodedata

# Página inicial
def home(request):
    return render(request, 'loja_app/home.html')


def suplementos(request):
    return render(request, 'loja_app/suplementos.html')


# Performance Esportiva
def nutricao_para_atletas(request):
    return render(request, 'loja_app/nutricao_para_atletas.html')


def suplementacao_esportiva(request):
    return render(request, 'loja_app/suplementacao_esportiva.html')


def protocolo_de_treino(request):
    return render(request, 'loja_app/protocolo_de_treino.html')


def recuperacao_muscular(request):
    return render(request, 'loja_app/recuperacao_muscular.html')


# Nutrição Funcional
def alimentacao_alcalina(request):
    return render(request, 'loja_app/alimentacao_alcalina.html')


def fitoterapia(request):
    return render(request, 'loja_app/fitoterapia.html')


def protocolos_antiinflamatorios(request):
    return render(request, 'loja_app/protocolos_antiinflamatorios.html')


def alimentos_funcionais(request):
    return render(request, 'loja_app/alimentos_funcionais.html')


# Saúde
def saude(request):
    return render(request, 'loja_app/saude.html')


# Projetos
def projetos(request):
    return render(request, 'loja_app/projetos.html')


# Objetivos
def massa_magra(request):
    return render(request, 'loja_app/massa_magra.html')


def definicao_muscular(request):
    return render(request, 'loja_app/definicao_muscular.html')


def emagrecimento_saudavel(request):
    return render(request, 'loja_app/emagrecimento_saudavel.html')


def energia_disposicao(request):
    return render(request, 'loja_app/energia_e_disposicao.html')


# Receitas Medicinais (Sub-Abas)
def receita_1(request):
    return render(request, 'loja_app/receita_1.html')


def receita_2(request):
    return render(request, 'loja_app/receita_2.html')


# Pesquisas Científicas (Sub-Abas)
def pesquisa_1(request):
    return render(request, 'loja_app/pesquisa_1.html')


def pesquisa_2(request):
    return render(request, 'loja_app/pesquisa_2.html')


# Consultas
@login_required
def agendamento_online(request):
    return render(request, 'loja_app/agendamento_online.html')

@login_required
def avaliacao_fisica(request):
    return render(request, 'loja_app/avaliacao_fisica.html')

@login_required
def planos_alimentares(request):
    return render(request, 'loja_app/planos_alimentares.html')


# Quem Somos
def quem_sou_eu(request):
    return render(request, 'loja_app/quem_sou_eu.html')


def quem_somos_nos(request):
    return render(request, 'loja_app/quem_somos_nos.html')


def conhecimento_na_pratica(request):
    return render(request, 'loja_app/conhecimento_na_pratica.html')


def normas_e_regulamento(request):
    return render(request, 'loja_app/normas_e_regulamento.html')


def conheca_nosso_trabalho(request):
    return render(request, 'loja_app/conheca_nosso_trabalho.html')

@login_required
def sobre_mim(request):
    return render(request, 'loja_app/sobre_mim.html')


def remedios_naturais_que_a_ciencia_comprova(request):
    return render(request, 'loja_app/remedios_naturais_que_a_ciencia_comprova.html')


def comprovacao_cientifica(request):
    return render(request, 'loja_app/comprovacao_cientifica.html')


def receitas_para_imunidade(request):
    return render(request, 'loja_app/receitas_para_imunidade.html')


def doencas_comuns_e_solucoes_naturais(request):
    return render(request, 'loja_app/doencas_comuns_e_solucoes_naturais.html')


def guia_de_ervas_medicinais(request):
    return render(request, 'loja_app/guia_de_ervas_medicinais.html')


def entenda_doencas_e_causas(request):
    return render(request, 'loja_app/entenda_doencas_e_causas.html')


def informativo(request):
    return render(request, 'loja_app/informativo.html')


def ebooks_exclusivos(request):
    return render(request, 'loja_app/ebooks_exclusivos.html')


def treinos_personalizados(request):
    return render(request, 'loja_app/treinos_personalizados.html')


def equipamentos_fitness(request):
    return render(request, 'loja_app/equipamentos_fitness.html')


def produtos_corporais(request):
    return render(request, 'loja_app/produtos_corporais.html')


def produtos_naturais(request):
    return render(request, 'loja_app/produtos_naturais.html')


@login_required
def adicionar_ao_carrinho(request, produto_id):
    # Obtenha o carrinho da sessão (se não houver, inicie como um dicionário vazio)
    carrinho = request.session.get('carrinho', {})

    # Se o produto já estiver no carrinho, aumente a quantidade
    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        # Caso contrário, adicione o produto com quantidade 1
        carrinho[str(produto_id)] = 1

    # Salve o carrinho de volta na sessão
    request.session['carrinho'] = carrinho

    # Redirecione para a página do carrinho
    return redirect('carrinho')

@login_required
def carrinho(request):
    # Pegando o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Inicializando o total
    total = 0
    produtos = []

    # Se o carrinho não estiver vazio
    if carrinho:
        for produto_id, quantidade in carrinho.items():
            # Aqui você pode buscar o produto no banco de dados usando o `produto_id`
            produto = get_object_or_404(Produto, id=produto_id)
            produtos.append({
                'produto': produto,
                'quantidade': quantidade,
                'total_item': produto.preco * quantidade,
            })
            total += produto.preco * quantidade
    else:
        produtos = None  # Quando o carrinho estiver vazio, você pode retornar None ou uma lista vazia

    return render(request, 'loja_app/carrinho.html', {'produtos': produtos, 'total': total})
@login_required
def remover_do_carrinho(request, carrinho_id):
    carrinho = Carrinho.objects.get(id=carrinho_id)
    carrinho.delete()
    return redirect('carrinho')  # Redireciona para a página do carrinho


def produtos(request):
    ebooks = [
        {
            "nome": "Abcesso - Definição e Causas",
            "arquivo": "Abcesso-Definicao-e-Causas.pdf",
            "imagem": "ebook1.jpg",
            "preco": 19.90,
            "descricao": "Este ebook aborda as principais causas e definições sobre abcessos e suas implicações na saúde."
        },
        {
            "nome": "Ácidos e Alcalis - Uma Introdução",
            "arquivo": "Acidos-e-Alcalis-Uma-Introducao.pdf",
            "imagem": "ebook2.jpg",
            "preco": 24.90,
            "descricao": "Entenda os conceitos básicos de ácidos e alcalis e sua importância na alimentação."
        },
        {
            "nome": "Código de Ética do Nutricionista",
            "arquivo": "codigo-de-etica-do-nutricionista.pdf",
            "imagem": "ebook3.jpg",
            "preco": 15.90,
            "descricao": "Este ebook detalha o código de ética que rege a profissão de nutricionista."
        },
        {
            "nome": "Guia Alimentar da População Brasileira",
            "arquivo": "ebook-guia-alimentar-da-população-brasileira.pdf",
            "imagem": "ebook4.jpg",
            "preco": 39.90,
            "descricao": "Conheça as diretrizes alimentares para uma vida saudável e balanceada."
        },
        {
            "nome": "Exercício Ilegal da Profissão",
            "arquivo": "exercicio-ilegal-da-profissao.pdf",
            "imagem": "ebook5.jpg",
            "preco": 29.90,
            "descricao": "Este ebook discute as implicações do exercício ilegal da profissão de nutricionista."
        },
        {
            "nome": "Frutas que Combatem o Ácido Úrico",
            "arquivo": "Frutas-que-Combatem-o-Acido-Urico.pdf",
            "imagem": "ebook6.jpg",
            "preco": 19.90,
            "descricao": "Aprenda sobre as frutas que ajudam a combater o ácido úrico e promovem a saúde."
        },
        {
            "nome": "Tabela de Honorários 2024",
            "arquivo": "tabela-de-honorarios-2024.pdf",
            "imagem": "ebook7.jpg",
            "preco": 9.90,
            "descricao": "Este ebook traz a tabela de honorários atualizada para profissionais de nutrição em 2024."
        },
    ]
    return render(request, 'loja_app/produtos.html', {'ebooks': ebooks})

@login_required(login_url='login')  # Redireciona para a página de login se o usuário não estiver autenticado
def finalizar_compra(request):
    try:
        # Busca pedido aberto (não finalizado) do usuário
        pedido = Pedido.objects.get(usuario=request.user, finalizado=False)
    except Pedido.DoesNotExist:
        # Cria novo pedido se não existir
        pedido = Pedido.objects.create(usuario=request.user, finalizado=False, total=Decimal(0))

    carrinho = Carrinho.objects.filter(usuario=request.user)
    total = Decimal(0)

    for item in carrinho:
        PedidoProduto.objects.create(
            pedido=pedido,
            produto=item.produto,
            quantidade=item.quantidade
        )
        total += item.total()

    pedido.total = total
    pedido.finalizado = True  # Marca o pedido como finalizado
    pedido.save()

    # Limpa o carrinho após finalizar o pedido
    carrinho.delete()

    return render(request, 'finalizar_compra.html', {'pedido': pedido})

def atualizar_quantidade_carrinho(request, carrinho_id):
    if request.is_ajax() and request.method == 'POST':
        nova_quantidade = int(request.POST.get('quantidade'))
        carrinho_item = get_object_or_404(Carrinho, id=carrinho_id)
        carrinho_item.quantidade = nova_quantidade
        carrinho_item.save()

        total_item = carrinho_item.produto.preco * carrinho_item.quantidade
        carrinho_total = sum(item.produto.preco * item.quantidade for item in Carrinho.objects.filter(usuario=request.user))

        # Formata os valores como moeda brasileira
        total_item_formatado = format_currency(total_item, 'BRL', locale='pt_BR')
        carrinho_total_formatado = format_currency(carrinho_total, 'BRL', locale='pt_BR')

        return JsonResponse({
            'total_item': total_item_formatado,
            'total_carrinho': carrinho_total_formatado
        })
    
def way_protein(request):
    return render(request, 'loja_app/way_protein.html')


def creatinas(request):
    return render(request, 'loja_app/creatinas.html')  # ou o caminho correto do seu template

def pre_treino(request):
    return render(request, 'loja_app/pre_treino.html')

def emagrecedores(request):
    return render(request, 'loja_app/emagrecedores.html')

def acessorios(request):
    return render(request, 'loja_app/acessorios.html')

def bcaa(request):
    return render(request, 'loja_app/bcaa.html')

def albumina(request):
    return render(request, 'loja_app/albumina.html')

def aumento_testosterona(request):
    return render(request, 'loja_app/aumento_testosterona.html')

def bebidas(request):
    return render(request, 'loja_app/bebidas.html')

def ciclistas(request):
    return render(request, 'loja_app/ciclistas.html')

def coffee(request):
    return render(request, 'loja_app/coffee.html')

def colageno(request):
    return render(request, 'loja_app/colageno.html')

def dose_unica(request):
    return render(request, 'loja_app/dose_unica.html')

def melatonina(request):
    return render(request, 'loja_app/melatonina.html')

def forca_energia(request):
    return render(request, 'loja_app/forca_energia.html')

def vitaminas(request):
    return render(request, 'loja_app/vitaminas.html')

def aumentar_massa_muscular(request):
    return render(request, 'loja_app/aumentar_massa_muscular.html')

def aminoacidos(request):
    return render(request, 'loja_app/aminoacidos.html')

def articulacoes_saudaveis(request):
    return render(request, 'loja_app/articulacoes_saudaveis.html')

def barras_de_proteinas(request):
    return render(request, 'loja_app/barras_de_proteinas.html')

def antioxidantes(request):
    return render(request, 'loja_app/antioxidantes.html')

def carboidratos(request):
    return render(request, 'loja_app/carboidratos.html')

def glutaminas(request):
    return render(request, 'loja_app/glutaminas.html')

def pastas_de_amendoim(request):
    return render(request, 'loja_app/pastas_de_amendoim.html')

def caldas_e_molhos(request):
    return render(request, 'loja_app/caldas_e_molhos.html')

def snacks_doces(request):
    return render(request, 'loja_app/snacks_doces.html')

def combos(request):
    return render(request, 'loja_app/combos.html')

def omega_3(request):
    # Lógica da view aqui
    return render(request, 'loja_app/omega3.html')

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")
        
        # Padroniza: minúsculo e sem acentos
def remover_acentos(texto):
    # Normaliza e remove os acentos do texto
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")
        
        texto = remover_acentos(message.lower())

        # Regras simples de resposta
        if "ola" in texto or "oi" in texto:
            resposta = "Olá! Seja bem-vindo ao Nutri Amorim 😊"
        elif "produto" in texto or "vender" in texto:
            resposta = "Vendemos suplementos, produtos naturais, roupas, acessórios e muito mais! Visite nossa página de produtos."
        elif "horario" in texto or "funciona" in texto or "atendimento" in texto:
            resposta = "Nosso horário de atendimento é de segunda a sexta, das 8h às 18h."
        elif "nutricionista" in texto:
            resposta = "Sim, temos atendimentos com nutricionista. Você pode agendar pela aba Consultas."
        elif "obrigado" in texto or "valeu" in texto:
            resposta = "De nada! Qualquer dúvida estou por aqui. 🌿"
        elif "tchau" in texto or "ate mais" in texto:
            resposta = "Até logo! Cuide bem da sua saúde! 🌱"
        else:
            resposta = (
                "Ainda estou aprendendo! Você pode visitar o menu lateral ou me perguntar sobre produtos, horários, "
                "consultas ou dúvidas comuns."
            )

        return JsonResponse({"response": resposta})

    return JsonResponse({"response": "Método não suportado."})

from django.shortcuts import render
from datetime import datetime

def avaliacao_receitas_med_view(request):
    resultado = None
    nome = ''
    idade = None
    imc = ''
    risco_doencas = []
    data_nascimento = ''
    idade_digitada = ''
    peso = ''
    altura = ''
    pressao = ''
    atividade = ''
    detalhes_resultado = ''

    # Variáveis extras para cálculo avançado
    peso_desejado = None
    peso_diferenca = None
    porcentagem_perda = None
    tmb = None
    get = None
    plano_kcal = None
    tempo_lento = None
    tempo_rapido = None
    sexo = ''
    doenca = ''
    medicacao = ''
    sono = None
    estresse = None
    percent_gc = None

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        data_nascimento = request.POST.get('data_nascimento', '')
        idade_digitada = request.POST.get('idade', '')
        peso = request.POST.get('peso', '')
        altura = request.POST.get('altura', '')
        pressao = request.POST.get('pressao', '')
        atividade = request.POST.get('atividade', '')
        sexo = request.POST.get('sexo', '')
        doenca = request.POST.get('doenca', '').strip()
        medicacao = request.POST.get('medicacao', '').strip()
        sono_raw = request.POST.get('sono', '')
        estresse_raw = request.POST.get('estresse', '')
        peso_desejado_raw = request.POST.get('peso_desejado', '')

        try:
            # Calcula idade
            if data_nascimento:
                nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
                hoje = datetime.today()
                idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            elif idade_digitada:
                idade = int(idade_digitada)
            else:
                idade = None  # Idade não informada

            # Converte dados numéricos
            peso_float = float(peso)
            altura_m = float(altura)  # altura em metros
            peso_desejado = float(peso_desejado_raw) if peso_desejado_raw else None
            sono = int(sono_raw) if sono_raw else None
            estresse = int(estresse_raw) if estresse_raw else None

            # Calcula IMC
            imc_float = round(peso_float / (altura_m ** 2), 1)
            imc = imc_float

            # Classificação IMC
            if imc_float < 18.5:
                classificacao_imc = "Magreza"
            elif imc_float < 25:
                classificacao_imc = "Peso normal ✅"
            elif imc_float < 30:
                classificacao_imc = "Sobrepeso"
            elif imc_float < 35:
                classificacao_imc = "Obesidade grau I"
            elif imc_float < 40:
                classificacao_imc = "Obesidade grau II"
            else:
                classificacao_imc = "Obesidade grau III"

            # Peso a ganhar/perder e % de perda desejada
            peso_diferenca = None
            porcentagem_perda = None
            if peso_desejado is not None:
                peso_diferenca = round(peso_desejado - peso_float, 1)  # positivo se ganho, negativo se perda
                if peso_diferenca < 0:
                    porcentagem_perda = round(abs(peso_diferenca) / peso_float * 100, 1)
                else:
                    porcentagem_perda = 0

            # Sexo numérico para %GC
            if sexo == 'masculino':
                sexo_num = 1
            else:
                sexo_num = 0

            # Cálculo do %GC (Percentual de Gordura Corporal)
            if idade is not None:
                percent_gc = round((1.2 * imc_float) + (0.23 * idade) - (10.8 * sexo_num) - 5.4, 1)

            # Cálculo da TMB (Mifflin-St Jeor)
            if sexo == 'masculino':
                tmb_calc = 10 * peso_float + 6.25 * (altura_m * 100) - 5 * idade + 5
            elif sexo == 'feminino':
                tmb_calc = 10 * peso_float + 6.25 * (altura_m * 100) - 5 * idade - 161
            else:
                tmb_masc = 10 * peso_float + 6.25 * (altura_m * 100) - 5 * idade + 5
                tmb_fem = 10 * peso_float + 6.25 * (altura_m * 100) - 5 * idade - 161
                tmb_calc = (tmb_masc + tmb_fem) / 2
            tmb = round(tmb_calc, 0)

            # Fator de atividade
            fator_atividade = 1.55 if atividade == '1' else 1.2

            # GET - gasto energético total
            get_calc = tmb * fator_atividade
            get = round(get_calc, 0)

            # Plano alimentar para perda lenta: GET - 500 kcal (ajustável)
            if peso_diferenca is not None and peso_diferenca < 0:
                plano_kcal = round(get - 500, 0)
                # 1 kg gordura = 7700 kcal
                semanas_lentas = abs(peso_diferenca) * 7700 / 500
                semanas_rapidas = abs(peso_diferenca) * 7700 / 1000
                tempo_lento = int(semanas_lentas)
                tempo_rapido = int(semanas_rapidas)
            else:
                plano_kcal = get
                tempo_lento = None
                tempo_rapido = None

            # Avaliação de risco
            risco = 0
            risco_doencas.clear()
            if idade is not None:
                if idade > 60:
                    risco += 1
                    risco_doencas.append("Idade avançada ❌")
                else:
                    risco_doencas.append("Idade abaixo de 60 anos ✅")
            else:
                risco_doencas.append("Idade não informada")

            if imc_float > 30:
                risco += 1
                risco_doencas.append("Obesidade ❌")
            else:
                risco_doencas.append("IMC adequado ✅")

            if pressao == '1':
                risco += 1
                risco_doencas.append("Hipertensão ❌")
            else:
                risco_doencas.append("Pressão arterial normal ✅")

            if atividade == '0':
                risco += 1
                risco_doencas.append("Sedentarismo ❌")
            else:
                risco_doencas.append("Pratica atividade física ✅")

            if risco >= 2:
                resultado = "Alto risco nutricional. Procure um profissional!"
            else:
                resultado = "Baixo risco nutricional. Continue com bons hábitos!"

            # Montar detalhes para o resultado (html safe)
            detalhes_resultado = (
                f"🧮 Classificação do IMC ({imc_float}): <strong>{classificacao_imc}</strong><br><br>"
                f"🩺 Classificação de Risco Nutricional:<br>"
            )
            for item in risco_doencas:
                detalhes_resultado += f"{item}<br>"
            detalhes_resultado += f"<br>🟢 Resultado: {resultado}"

        except Exception as e:
            resultado = "Erro ao processar os dados. Verifique os campos."
            detalhes_resultado = f"Detalhes do erro: {e}"

    return render(request, 'loja_app/avaliacao_receitas_med.html', {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'idade': idade,
        'idade_digitada': idade_digitada,
        'peso': peso,
        'altura': altura,
        'peso_desejado': peso_desejado,
        'pressao': pressao,
        'atividade': atividade,
        'sexo': sexo,
        'doenca': doenca,
        'medicacao': medicacao,
        'sono': sono,
        'estresse': estresse,
        'imc': imc,
        'classificacao': classificacao_imc if 'classificacao_imc' in locals() else '',
        'peso_diferenca': peso_diferenca,
        'porcentagem_perda': porcentagem_perda,
        'tmb': tmb,
        'get': get,
        'plano_kcal': plano_kcal,
        'tempo_lento': tempo_lento,
        'tempo_rapido': tempo_rapido,
        'resultado': resultado,
        'risco_doencas': risco_doencas,
        'detalhes_resultado': detalhes_resultado,
        'percent_gc': percent_gc,
    })