from flask import Blueprint, render_template

# ===== CRIA O BLUEPRINT =====
rotas = Blueprint('rotas', __name__)

# ============================================================
# ===== ROTA PRINCIPAL =====
# ============================================================

@rotas.route("/")
def index():
    return render_template("index.html")


# ============================================================
# ===== ROTAS DAS CATEGORIAS =====
# ============================================================

@rotas.route("/categoria1")
def categoria1():
    return render_template("categoria1.html")

@rotas.route("/categoria2")
def categoria2():
    return render_template("categoria2.html")

@rotas.route("/categoria3")
def categoria3():
    return render_template("categoria3.html")

@rotas.route("/categoria4")
def categoria4():
    return render_template("categoria4.html")

@rotas.route("/categoria5")
def categoria5():
    return render_template("categoria5.html")

@rotas.route("/categoria6")
def categoria6():
    return render_template("categoria6.html")

@rotas.route("/categoria7")
def categoria7():
    return render_template("categoria7.html")

@rotas.route("/categoria8")
def categoria8():
    return render_template("categoria8.html")


# ============================================================
# ===== ROTA DA PASTA PROGRAMACAO (RPG) =====
# ============================================================

@rotas.route("/programacao/")
@rotas.route("/programacao/indexprogramacao.html")
def programacao():
    return render_template("categoria2.html")


# ============================================================
# ===== ROTA 404 (PÁGINA NÃO ENCONTRADA) =====
# ============================================================

@rotas.app_errorhandler(404)
def pagina_nao_encontrada(e):
    return "<h1>🚫 Página não encontrada</h1><p><a href='/'>Voltar para o início</a></p>", 404


# ============================================================
# ===== ROTA DE TESTE (opcional) =====
# ============================================================

@rotas.route("/teste")
def teste():
    return """
    <h1>✅ Servidor funcionando!</h1>
    <p>Rotas disponíveis:</p>
    <ul>
        <li><a href='/'>/</a> - Página inicial</li>
        <li><a href='/categoria1'>/categoria1</a> - Minha História</li>
        <li><a href='/categoria2'>/categoria2</a> - RPG Programação</li>
        <li><a href='/categoria3'>/categoria3</a> - Projetos</li>
        <li><a href='/categoria4'>/categoria4</a> - Contato</li>
        <li><a href='/categoria5'>/categoria5</a> - Blog</li>
        <li><a href='/categoria6'>/categoria6</a> - Tecnologias</li>
        <li><a href='/categoria7'>/categoria7</a> - Trajetória</li>
        <li><a href='/categoria8'>/categoria8</a> - Recomendações</li>
        <li><a href='/programacao/'>/programacao/</a> - RPG (mesmo que categoria2)</li>
    </ul>
    """


# ============================================================
# ===== ROTA PARA ARQUIVOS ESTÁTICOS (imagens, etc) =====
# ============================================================

# Isso já é automático no Flask, não precisa criar rota
# Mas se quiser forçar, pode fazer:
# @rotas.route("/static/<path:filename>")
# def static_files(filename):
#     from flask import send_from_directory
#     return send_from_directory("static", filename)