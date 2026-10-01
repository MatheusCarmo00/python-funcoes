def calcular_preco(preco, vendas):
    if vendas < 500 and preco < 30:
        novo_preco = preco * 1.10
    elif vendas >= 500 and vendas < 1000 and preco >= 30 and preco < 80:
        novo_preco = preco * 1.15
    elif vendas >= 1000 and preco >= 80:
        novo_preco = preco * 0.95
    else:
        novo_preco = preco

    print(f"Novo preço: R$ {novo_preco:.2f}")


def main():
    preco = float(input("Digite o preço atual: R$ "))
    vendas = int(input("Digite a média mensal de vendas: "))

    calcular_preco(preco, vendas)


main()