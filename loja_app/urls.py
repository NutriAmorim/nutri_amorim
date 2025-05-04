from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Vendas no site
    path(
        'suplementos/',
        views.suplementos,
        name='suplementos'
    ),
    path(
        'produtos_naturais/',
        views.produtos_naturais,
        name='produtos_naturais'
    ),
    path(
        'produtos_corporais/',
        views.produtos_corporais,
        name='produtos_corporais'
    ),
    path(
        'equipamentos_fitness/',
        views.equipamentos_fitness,
        name='equipamentos_fitness'
    ),
    path(
        'treinos_personalizados/',
        views.treinos_personalizados,
        name='treinos_personalizados'
    ),
    path(
        'ebooks_exclusivos/',
        views.ebooks_exclusivos,
        name='ebooks_exclusivos'
    ),

    # Performance Esportiva
    path(
        'nutricao-para-atletas/',
        views.nutricao_para_atletas,
        name='nutricao_para_atletas'
    ),
    path(
        'suplementacao-esportiva/',
        views.suplementacao_esportiva,
        name='suplementacao_esportiva'
    ),
    path(
        'protocolo-de-treino/',
        views.protocolo_de_treino,
        name='protocolo_de_treino'
    ),
    path(
        'recuperacao-muscular/',
        views.recuperacao_muscular,
        name='recuperacao_muscular'
    ),

    # Nutrição Funcional
    path(
        'alimentacao-alcalina/',
        views.alimentacao_alcalina,
        name='alimentacao_alcalina'
    ),
    path(
        'fitoterapia/',
        views.fitoterapia,
        name='fitoterapia'
    ),
    path(
        'protocolos-antiinflamatorios/',
        views.protocolos_antiinflamatorios,
        name='protocolos_antiinflamatorios'
    ),
    path(
        'alimentos-funcionais/',
        views.alimentos_funcionais,
        name='alimentos_funcionais'
    ),

    # Objetivos
    path(
        'massa-magra/',
        views.massa_magra,
        name='massa_magra'
    ),
    path(
        'definicao-muscular/',
        views.definicao_muscular,
        name='definicao_muscular'
    ),
    path(
        'emagrecimento-saudavel/',
        views.emagrecimento_saudavel,
        name='emagrecimento_saudavel'
    ),
    path(
        'energia-disposicao/',
        views.energia_disposicao,
        name='energia_disposicao'
    ),

    # Receitas Medicinais
    path(
        'informativo',
        views.informativo,
        name='informativo'
    ),
    path(
        'entenda_doencas_e_causas',
        views.entenda_doencas_e_causas,
        name='entenda_doencas_e_causas'
    ),
    path(
        'guia_de_ervas_medicinais/',
        views.guia_de_ervas_medicinais,
        name='guia_de_ervas_medicinais'
    ),
    path(
        'doencas_comuns_e_solucoes_naturais/',
        views.doencas_comuns_e_solucoes_naturais,
        name='doencas_comuns_e_solucoes_naturais'
    ),
    path(
        'receitas_para_imunidade/',
        views.receitas_para_imunidade,
        name='receitas_para_imunidade'
    ),

    # Pesquisas Científicas
    path(
        'comprovacao_cientifica/',
        views.comprovacao_cientifica,
        name='comprovacao_cientifica'
    ),
    path(
        'remedios_naturais_que_a_ciencia_comprova/',
        views.remedios_naturais_que_a_ciencia_comprova,
        name='remedios_naturais_que_a_ciencia_comprova'
    ),

    # Consultas
    path(
        'agendamento-online/',
        views.agendamento_online,
        name='agendamento_online'
    ),
    path(
        'avaliacao-fisica/',
        views.avaliacao_fisica,
        name='avaliacao_fisica'
    ),
    path(
        'planos-alimentares/',
        views.planos_alimentares,
        name='planos_alimentares'
    ),

    # Quem Somos
    path(
        'sobre_mim/',
        views.sobre_mim,
        name='sobre_mim'
    ),
    path(
        'conheca_nosso_trabalho/',
        views.conheca_nosso_trabalho,
        name='conheca_nosso_trabalho'
    ),
    path(
        'normas_e_regulamento/',
        views.normas_e_regulamento,
        name='normas_e_regulamento'
    ),
    path(
        'conhecimento_na_pratica/',
        views.conhecimento_na_pratica,
        name='conhecimento_na_pratica'
    ),

    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('remover_do_carrinho/<int:carrinho_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('produtos/', views.produtos, name='produtos'),
    path('atualizar_quantidade_carrinho/<int:carrinho_id>/', views.atualizar_quantidade_carrinho, name='atualizar_quantidade_carrinho'),
    path('way_protein/', views.way_protein, name='way_protein'),
    path('creatinas/', views.creatinas, name='creatinas'),
    path('pre_treino/', views.pre_treino, name='pre_treino'),
    path('emagrecedores/', views.emagrecedores, name='emagrecedores'),
    path('acessorios/', views.acessorios, name='acessorios'),
    path('bcaa/', views.bcaa, name='bcaa'),
    path('albumina/', views.albumina, name='albumina'),
    path('aumento_testosterona/', views.aumento_testosterona, name='aumento_testosterona'),
    path('bebidas/', views.bebidas, name='bebidas'),
    path('ciclistas/', views.ciclistas, name='ciclistas'),
    path('coffee/', views.coffee, name='coffee'),
    path('colageno/', views.colageno, name='colageno'),
    path('dose-unica/', views.dose_unica, name='dose_unica'),
    path('melatonina/', views.melatonina, name='melatonina'),
    path('forca-energia/', views.forca_energia, name='forca_energia'),
    path('vitaminas/', views.vitaminas, name='vitaminas'),
    path('aumentar-massa-muscular/', views.aumentar_massa_muscular, name='aumentar_massa_muscular'),
    path('aminoacidos/', views.aminoacidos, name='aminoacidos'),
    path('articulacoes-saudaveis/', views.articulacoes_saudaveis, name='articulacoes_saudaveis'),
    path('barras-de-proteinas/', views.barras_de_proteinas, name='barras_de_proteinas'),
    path('antioxidantes/', views.antioxidantes, name='antioxidantes'),
    path('carboidratos/', views.carboidratos, name='carboidratos'),
    path('glutaminas/', views.glutaminas, name='glutaminas'),
    path('pastas-de-amendoim/', views.pastas_de_amendoim, name='pastas_de_amendoim'),
    path('caldas-e-molhos/', views.caldas_e_molhos, name='caldas_e_molhos'),
    path('snacks-doces/', views.snacks_doces, name='snacks_doces'),
    path('combos/', views.combos, name='combos'),
    path('omega_3/', views.omega_3, name='omega_3'),
    path('creatinas/', views.creatinas, name='Creatinas')
]

