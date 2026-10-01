def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado


def main():
    numero = int(input("Digite um número inteiro: "))

    resultado = fatorial(numero)

    print(f"{numero}! = {resultado}")


main()