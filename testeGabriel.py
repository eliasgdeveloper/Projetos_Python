# import requests
# from bs4 import BeautifulSoup
#
# url = "https://lista.mercadolivre.com.br/notebook"
#
# headers = {"User-Agent": "Mozilla/5.0"}
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
#
# listaProdutos = []
#
# for product in soup.find_all("div", class_="ui-search-result__content-wrapper"):
#     title = product.find("h2").text.strip()
#     price = product.find("span", class_="andes-money-amount__fraction")
#     price = price.text.strip() if price else "Preço não disponível"
#
#     listaProdutos.append((title, "R$ " + price))  # Adicionando como tupla
#
# # Exibir os produtos
# for produto in listaProdutos:
#     print(produto[0], "-", produto[1])

def soma_numeros2():
    num1 = float(input("Digite um número: "))  # Converter para float antes de usar round
    num2 = float(input("Digite um número: "))

    num1_round = round(num1, 1)  # Agora funciona corretamente
    num2_round = round(num2, 1)

    print (round(num1_round + num2_round, 1))  # Realiza a soma corretamente

soma_numeros2()
