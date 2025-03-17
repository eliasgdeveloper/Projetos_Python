import random
import tkinter.messagebox as msgbox
import tkinter.simpledialog as simpledialog

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]

    # Janela de boas-vindas
    msgbox.showinfo("Pedra, Papel e Tesoura", "Bem-vindo ao jogo!")

    # Perguntar ao jogador a escolha
    jogador = simpledialog.askstring("Escolha", "Digite pedra, papel ou tesoura:").lower()

    if jogador not in opcoes:
        msgbox.showwarning("Erro", "Escolha inválida! Tente novamente.")
        return

    # Escolha do computador
    computador = random.choice(opcoes)

    # Mostrar escolhas
    msgbox.showinfo("Escolhas", f"Você escolheu: {jogador}\nComputador escolheu: {computador}")

    # Verificação de vencedor
    if jogador == computador:
        resultado = "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        resultado = "Você venceu! 🎉"
    else:
        resultado = "Você perdeu! 😢"

    # Mostrar resultado final
    msgbox.showinfo("Resultado", resultado)

# Importante: Executar o jogo apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    jogar()
