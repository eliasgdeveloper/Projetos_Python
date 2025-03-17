import tkinter as tk
from tkinter import messagebox
import random

# Variáveis globais para pontuação
pontos_jogador = 0
pontos_pc = 0


def jogar(escolha_jogador):
    global pontos_jogador, pontos_pc
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_pc = random.choice(opcoes)

    # Verificação de vencedor
    if escolha_jogador == escolha_pc:
        resultado = "Empate!"
    elif (escolha_jogador == "pedra" and escolha_pc == "tesoura") or \
            (escolha_jogador == "papel" and escolha_pc == "pedra") or \
            (escolha_jogador == "tesoura" and escolha_pc == "papel"):
        resultado = "Você venceu! 🎉"
        pontos_jogador += 1
    else:
        resultado = "Você perdeu! 😢"
        pontos_pc += 1

    # Atualiza os labels de pontuação
    label_pontos_jogador.config(text=f"Você: {pontos_jogador}")
    label_pontos_pc.config(text=f"PC: {pontos_pc}")

    # Exibe o resultado
    label_resultado.config(text=f"Você escolheu: {escolha_jogador}\nPC escolheu: {escolha_pc}\n{resultado}")


def resetar():
    global pontos_jogador, pontos_pc
    pontos_jogador = 0
    pontos_pc = 0
    label_pontos_jogador.config(text="Você: 0")
    label_pontos_pc.config(text="PC: 0")
    label_resultado.config(text="")


# Configuração da janela principal
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")
root.geometry("400x400")
root.configure(bg="#f5f5f5")

# Layout
frame_top = tk.Frame(root, bg="#222", height=50)
frame_top.pack(fill=tk.X)

label_pontos_jogador = tk.Label(frame_top, text="Você: 0", fg="white", bg="#222", font=("Arial", 12, "bold"))
label_pontos_jogador.pack(side=tk.LEFT, padx=20)

label_pontos_pc = tk.Label(frame_top, text="PC: 0", fg="white", bg="#222", font=("Arial", 12, "bold"))
label_pontos_pc.pack(side=tk.RIGHT, padx=20)

frame_jogo = tk.Frame(root, bg="#f5f5f5")
frame_jogo.pack(pady=20)

label_instrucao = tk.Label(frame_jogo, text="Escolha uma opção:", font=("Arial", 14))
label_instrucao.pack()

frame_botoes = tk.Frame(frame_jogo)
frame_botoes.pack()

botao_pedra = tk.Button(frame_botoes, text="✊ Pedra", font=("Arial", 12), bg="#20b2aa", fg="white", width=10,
                        command=lambda: jogar("pedra"))
botao_pedra.grid(row=0, column=0, padx=10, pady=10)

botao_papel = tk.Button(frame_botoes, text="✋ Papel", font=("Arial", 12), bg="#ff6347", fg="white", width=10,
                        command=lambda: jogar("papel"))
botao_papel.grid(row=0, column=1, padx=10, pady=10)

botao_tesoura = tk.Button(frame_botoes, text="✌️ Tesoura", font=("Arial", 12), bg="#9acd32", fg="white", width=10,
                          command=lambda: jogar("tesoura"))
botao_tesoura.grid(row=0, column=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5")
label_resultado.pack(pady=10)

botao_reset = tk.Button(root, text="🔄 Resetar", font=("Arial", 12), bg="#808080", fg="white", command=resetar)
botao_reset.pack(pady=10)

root.mainloop()
