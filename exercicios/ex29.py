def calcular_investimento(tipo, valor):
    if tipo == 1:
        rendimento = valor * 0.03
        valor_corrigido = valor + rendimento
        print(f"Valor corrigido: R$ {valor_corrigido:.2f}")

    elif tipo == 2:
        rendimento = valor * 0.05
        valor_corrigido = valor + rendimento
        print(f"Valor corrigido: R$ {valor_corrigido:.2f}")

    else:
        print("Tipo de investimento inválido.")


def main():
    tipo = int(input("Digite o tipo de investimento (1 ou 2): "))
    valor = float(input("Digite o valor investido: R$ "))

    calcular_investimento(tipo, valor)


main()