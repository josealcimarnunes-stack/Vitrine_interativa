from flask import Flask, render_template

app = Flask(__name__)

# Desativa cache para desenvolvimento
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.after_request
def after_request(response):
    """Força o navegador a não cachear nada"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print("=" * 50)
    print("🚀 VITRINE INTERATIVA")
    print("=" * 50)
    print("🔗 http://127.0.0.1:5000")
    print("=" * 50)
    print("🔄 Cache desativado (desenvolvimento)")
    print("🔄 Hard Refresh: Ctrl+F5")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
