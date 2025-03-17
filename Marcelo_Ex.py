numero = '123-4'
titular = 'João Lucas'
saldo = 1200.0
limite = 3000.0
despesas = 1080.0

if saldo < despesas:
    print("Saldo insuficiente")
else:
    print("Compra efetuada com sucesso")
    saldo_atual = saldo - despesas

print("Número:", numero)
print("Titular:", titular)
if saldo >= despesas:
    print("Saldo atual:", saldo_atual)
else:
    print("Saldo atual:", saldo)
print("Limite:", limite)





frutas = ["maçã", "banana", "laranja", "uva"]


fruta_buscada = input("Digite o nome de uma fruta: ").strip().lower()


try:

    indice_fruta = frutas.index(fruta_buscada)
    print(f'A fruta "{fruta_buscada}" está na posição {indice_fruta} da lista.')
except ValueError:

    print(f'A fruta "{fruta_buscada}" não foi encontrada na lista.')

    # Lista de produtos e preços
    Lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
    Preços = [2000, 9000, 6000, 11000]
    dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

    # Solicitar entrada do usuário para nome e preço do produto
    nome_produto = input("Nome do produto: ").strip().lower()
    preço_produto = input("Preço do produto: ").strip()

    # VALIDAÇÃO ADICIONADA: VERIFICA SE O PREÇO É UM NÚMERO VÁLIDO ANTES DE CONVERTÊ-LO
    if preço_produto.replace('.', '', 1).isdigit():
        preço_produto = float(preço_produto)  # Converte para float
    else:
        print("Erro: O preço deve ser um número válido.")
        exit()  # Sai do programa se a entrada for inválida

    # REMOVIDA LINHA REDUNDANTE QUE CONVERTIA NOVAMENTE `nome_produto` PARA MINÚSCULO
    # nome_produto = nome_produto.lower()

    # CORREÇÃO: `dic_produtos[Nome_produto]` FOI AJUSTADO PARA `dic_produtos[nome_produto]` E `Preço_produto` PARA `preço_produto`
    dic_produtos[nome_produto] = preço_produto
    print(dic_produtos)

    # Atualizar o preço de todos os produtos em 10% no final
    # REMOVIDO O TRECHO DUPLICADO QUE ATUALIZAVA O PREÇO DO PRODUTO "AIRPOD" DUAS VEZES
    for produto in dic_produtos:
        novo_preço = dic_produtos[produto] * 1.1  # Calcula 10% a mais
        dic_produtos[produto] = novo_preço  # Atualiza o preço no dicionário

    # EXIBE O DICIONÁRIO COM OS PREÇOS ATUALIZADOS
    print(dic_produtos)































# Lista de produtos e preços
Lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
Preços = [2000, 9000, 6000, 11000]
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# Solicitar entrada do usuário para nome e preço do produto
nome_produto = input("Nome do produto: ").strip().lower()
preço_produto = input("Preço do produto: ").strip()

# VALIDAÇÃO ADICIONADA: VERIFICA SE O PREÇO É UM NÚMERO VÁLIDO ANTES DE CONVERTÊ-LO
if preço_produto.replace('.', '', 1).isdigit():
    preço_produto = float(preço_produto)  # Converte para float
else:
    print("Erro: O preço deve ser um número válido.")
    exit()  # Sai do programa se a entrada for inválida

# REMOVIDA LINHA REDUNDANTE QUE CONVERTIA NOVAMENTE `nome_produto` PARA MINÚSCULO
# nome_produto = nome_produto.lower()

# CORREÇÃO: `dic_produtos[Nome_produto]` FOI AJUSTADO PARA `dic_produtos[nome_produto]` E `Preço_produto` PARA `preço_produto`
dic_produtos[nome_produto] = preço_produto
print(dic_produtos)

# Atualizar o preço de todos os produtos em 10% no final
# REMOVIDO O TRECHO DUPLICADO QUE ATUALIZAVA O PREÇO DO PRODUTO "AIRPOD" DUAS VEZES
for produto in dic_produtos:
    novo_preço = dic_produtos[produto] * 1.1  # Calcula 10% a mais
    dic_produtos[produto] = novo_preço  # Atualiza o preço no dicionário

# EXIBE O DICIONÁRIO COM OS PREÇOS ATUALIZADOS
print(dic_produtos)

