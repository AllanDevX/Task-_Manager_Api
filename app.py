# Importando Framework Flask
from flask import Flask

# Criando a instanica do Flask
app = Flask(__name__)

# Definição de rotas
@app.route("/")
def hello_world():
    return "Hello World!"

# Definição de rotas
@app.route("/about")
def about():
    return "Página sobre"

# Usando if para rodar o programa
if __name__ == "__main__":
    # app.run ativa o modo de depuração
    app.run(debug=True)