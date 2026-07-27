from flask import Flask
from rotas import rotas

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)