def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado


def dividir(numero1, numero2):
    return numero1 / numero2


def main():
    n = int(input("Digite o valor de N: "))

    resultado = 1

    for i in range(1, n + 1):
        fat = fatorial(i)
        resultado = resultado + dividir(1, fat)

    print(f"Resultado: {resultado}")


main()