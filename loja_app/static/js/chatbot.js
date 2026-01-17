// loja_app/static/js/chatbot.js

document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-log"); // aqui estava chat-box
    const chatInput = document.getElementById("chat-input");
    const chatSend = document.getElementById("chat-send");

    function adicionarMensagem(mensagem, remetente = "usuario") {
        const msgDiv = document.createElement("div");
        msgDiv.textContent = mensagem;
        msgDiv.className = remetente;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function enviarMensagem() {
        const mensagem = chatInput.value.trim();
        if (mensagem === "") return;

        adicionarMensagem(mensagem, "usuario");
        chatInput.value = "";

        fetch("/chatbot/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
            body: JSON.stringify({ message: mensagem }),
        })
        .then((res) => res.json())
        .then((data) => {
            adicionarMensagem(data.response, "bot");
        })
        .catch(() => {
            adicionarMensagem("Erro ao enviar mensagem.", "bot");
        });
    }

    chatSend.addEventListener("click", enviarMensagem);

    chatInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            enviarMensagem();
        }
    });

    function getCSRFToken() {
        const cookies = document.cookie.split(";").map(c => c.trim());
        for (let cookie of cookies) {
            if (cookie.startsWith("csrftoken=")) {
                return cookie.split("=")[1];
            }
        }
        return "";
    }
});