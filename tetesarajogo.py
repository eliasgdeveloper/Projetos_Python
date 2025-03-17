import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("Digite pedra, papel ou tesoura")
    print(f"Você escolheu: {jogador}")  # Apenas para mostrar que capturou corretamente
    if jogador not in opcoes:
        print("Erro. Escolha inválida! Tente novamente.")
        return
    computador = random.choice(opcoes)

    print(f"Escolhas", f"Você escolheu: {jogador}\nComputador escolheu: {computador}")

    if jogador == computador:
        resultado = "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        resultado = "Você venceu! 🎉"
    else:
        resultado = "Você perdeu! 😢"

    print("Resultado", resultado)

jogar()