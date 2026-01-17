# loja_app/chatbot.py
import json
import unicodedata
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))

@csrf_exempt
def chatbot_view(request):
    if request.method != "POST":
        return JsonResponse({"response": "Método não suportado."})

    try:
        data = json.loads(request.body)
        message = data.get("message", "")
        texto = remover_acentos(message.lower())

        if "ola" in texto or "oi" in texto:
            resposta = "Olá! Seja bem-vindo ao Nutri Amorim"

        elif "produto" in texto or "vender" in texto:
            resposta = (
                "Vendemos suplementos, produtos naturais, roupas, acessórios e muito mais. "
                "Visite nossa página de produtos."
            )

        elif "horario" in texto or "atendimento" in texto:
            resposta = "Atendemos de segunda a sexta, das 8h às 18h."

        elif "nutricionista" in texto:
            resposta = "Você pode agendar atendimento na aba Consultas."

        elif "obrigado" in texto or "valeu" in texto:
            resposta = "Por nada! Estou à disposição."

        elif "tchau" in texto:
            resposta = "Até logo! Cuide bem da sua saúde."

        else:
            resposta = "Não entendi bem. Pode reformular a pergunta?"

        return JsonResponse({"response": resposta})

    except Exception:
        return JsonResponse({"response": "Erro ao processar a mensagem."}, status=500)
