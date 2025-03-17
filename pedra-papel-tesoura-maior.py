import random
import tkinter as tk
from tkinter import messagebox, simpledialog  # Importação correta


def exibir_mensagem(resultado, jogador, computador):
    """Cria uma janela maior para mostrar o resultado do jogo"""
    janela = tk.Toplevel()
    janela.title("Resultado")
    janela.geometry("400x250")  # Define o tamanho da janela (Largura x Altura)

    # Texto dentro da janela
    label = tk.Label(janela, text=f"Você escolheu: {jogador}\n\nO computador escolheu: {computador}\n\n{resultado}",
                     font=("Arial", 14), justify="center", padx=20, pady=20)
    label.pack()

    # Botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), command=janela.destroy)
    botao_fechar.pack(pady=10)


def jogar():
    opcoes = ["pedra", "papel", "tesoura"]

    # Caixa de diálogo para o jogador escolher
    jogador = simpledialog.askstring("Escolha", "Digite pedra, papel ou tesoura:").lower()

    if jogador not in opcoes:
        messagebox.showwarning("Erro", "Escolha inválida! Tente novamente.")
        return

    # Escolha do computador
    computador = random.choice(opcoes)

    # Determinar o resultado
    if jogador == computador:
        resultado = "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
        resultado = "Você venceu! 🎉"
    else:
        resultado = "Você perdeu! 😢"

    # Chamar a função para exibir a janela com o resultado
    exibir_mensagem(resultado, jogador, computador)


# Configuração do Tkinter
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Mensagem de boas-vindas
messagebox.showinfo("Pedra, Papel e Tesoura", "Bem-vindo ao jogo!")

# Iniciar o jogo
jogar()

# Mantém a aplicação Tkinter rodando
root.mainloop()

