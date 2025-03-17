from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jogar", methods=["POST"])
def jogar():
    jogador = request.json.get("escolha")

    if jogador not in opcoes:
        return jsonify({"erro": "Escolha inválida!"})

    computador = random.choice(opcoes)

    if jogador == computador:
        resultado = "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
        resultado = "Você venceu! 🎉"
    else:
        resultado = "Você perdeu! 😢"

    return jsonify({"jogador": jogador, "computador": computador, "resultado": resultado})


if __name__ == "__main__":
    app.run(debug=True)
