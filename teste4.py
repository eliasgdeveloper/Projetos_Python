def jogar():
    opcoes = ["pedra", "papel", "tesoura"]

    # Perguntar ao jogador a escolha
    jogador = input("Digite pedra, papel ou tesoura: ").lower()
    print(f"Você escolheu: {jogador}")  # Apenas para mostrar que capturou corretamente

# Chamar a função para executar o jogo
jogar()
