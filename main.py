from flask import Flask, render_template
import os
import time
import threading
import requests

app = Flask(__name__)

# ============================================================
# CONFIGURAÇÕES
# ============================================================
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


# ============================================================
# DESATIVA CACHE
# ============================================================
@app.after_request
def after_request(response):
    """Força o navegador a não cachear nada"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    return response


# ============================================================
# KEEP-ALIVE - MANTÉM O APP ACORDADO NA RENDER
# ============================================================
def manter_acordado():
    """
    Faz uma requisição para o próprio servidor a cada 1 hora
    Isso evita que a Render coloque o app em modo "sleep"
    """
    # Pega a URL do ambiente (Render) ou usa localhost
    url = os.environ.get("RENDER_EXTERNAL_URL", "http://127.0.0.1:5000")
    url_ping = f"{url}/ping"

    print(f"⏰ Keep-alive iniciado!")
    print(f"📍 URL: {url_ping}")
    print(f"⏱️  Intervalo: 1 hora")

    while True:
        try:
            response = requests.get(url_ping, timeout=10)
            print(
                f"🔄 Keep-alive: {response.status_code} - {time.strftime('%d/%m/%Y %H:%M:%S')}"
            )
        except Exception as e:
            print(f"❌ Keep-alive erro: {e}")

        # Espera 1 hora (3600 segundos)
        time.sleep(3600)


# Inicia o keep-alive em uma thread separada (só se não for debug)
# Isso evita que o keep-alive rode duas vezes em desenvolvimento
if not app.debug:
    thread = threading.Thread(target=manter_acordado, daemon=True)
    thread.start()
    print("✅ Keep-alive thread iniciada!")
else:
    print("ℹ️  Keep-alive desativado (modo debug)")


# ============================================================
# ROTAS
# ============================================================
@app.route("/")
def index():
    """Página principal da vitrine"""
    return render_template("index.html")


@app.route("/ping")
def ping():
    """
    Rota de ping para verificar se o servidor está vivo
    Usada pelo keep-alive e por serviços de monitoramento
    """
    return "🏓 Pong! Servidor ativo!"


@app.route("/health")
def health():
    """
    Rota de saúde para a Render verificar se o app está rodando
    """
    return {"status": "ok", "timestamp": time.strftime("%d/%m/%Y %H:%M:%S")}


# ============================================================
# INICIALIZAÇÃO
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 VITRINE INTERATIVA")
    print("=" * 50)
    print("🔗 http://127.0.0.1:5000")
    print("=" * 50)
    print("🔄 Cache desativado (desenvolvimento)")
    print("🔄 Hard Refresh: Ctrl+F5")
    print("=" * 50)
    print("📍 Rotas disponíveis:")
    print("   /      - Página principal")
    print("   /ping  - Verifica se o servidor está vivo")
    print("   /health - Verifica a saúde do servidor")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
