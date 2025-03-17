'''num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)'''


'''idade = 15
print(f"Minha idade é {idade} anos.")
if idade < 18:
    print("Menor")'''

'''nota = 7
if nota >= 7:
    print("Aprovado")
    if nota < 7:
        print("Reprovado")'''

"""nota = 7

if nota >= 7 and nota <= 10:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
elif nota >= 0 and nota < 5:
    print("Reprovado")
else:
    print("Nota inválida")"""

"""nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")"""

# comentar Ctrl + / no Windows ou Linux, e Cmd + / no macOS.

# num1, num2 = 10, 20
# print(max(num1, num2))
#
# num1, num2 = 30, 5
# print(max(num1, num2))

# Exercício 5
# Exercício 5
# cor = "azul"
#
# if cor == "vermelho":
#     print("Pare")
# elif cor == "laranja":
#     print("Atenção")
# else:
#     print("Siga")

# Exercício 6
# temperatura = 28
#
# if temperatura > 30:
#     print("Muito quente!")
# else:
#     print("Temperatura agradável")


# Exercício 6
# fruta = "banana"
#
# if fruta == "maçã":
#     print("Você escolheu maçã")
# else:
#     print("Você escolheu outra fruta")

# Exercício 7
# numero = int(input("Digite um número: "))
#
# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")


# Exercício 8 combinado

# senha = "123456"  # senha correta com 6 números
# senha_digitada = input("Digite a senha (6 dígitos numéricos): ")
#
# if senha_digitada.isdigit() and len(senha_digitada) == 6:
#     if senha_digitada == senha:
#         print("Senha correta")
#     else:
#         print("Senha incorreta")
# else:
#     print("Senha inválida. A senha deve conter exatamente 6 dígitos numéricos.")


# Exercício 10 com mais condições
# a = 5
# b = 10
#
# if a == b:
#     print("Iguais")
# elif a > b:
#     print("a é maior que b")
# elif a < b:
#     print("a é menor que b")
# else:
#     print("Condição inesperada")


# Exercício 10 avançado

# a = input("Digite o valor de a: ")
# b = input("Digite o valor de b: ")
#
# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)
#
#     if a == b:
#         print("Iguais")
#     elif a > b:
#         print("a é maior que b")
#     else:
#         print("a é menor que b")
# else:
#     print("Valores inválidos")


# Exercício 12 com operadores lógicos


# altura = 1.75
# idade = 20
#
# # Pessoa alta e jovem (exemplo usando "and")
# if altura > 1.80 and idade < 25:
#     print("Pessoa alta e jovem")
#
# # Pessoa alta ou jovem (exemplo usando "or")
# elif altura > 1.80 or idade < 25:
#     print("Pessoa alta ou jovem")
#
# # Caso contrário
# else:
#     print("Pessoa com altura média ou baixa e com 25 anos ou mais")


# Exercício 13 avançado
cidade = "São Paulo"
estado = "SP"

# usando operadores lógicos e método lower()
if cidade.lower() == "rio" or cidade.lower() == "rio de janeiro":
    print("Você mora no Rio.")
elif cidade.lower() == "são paulo" and estado.upper() == "SP":
    print("Você mora em São Paulo - SP.")
else:
    print("Você mora em outra cidade ou estado.")


















