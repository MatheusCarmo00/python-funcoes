def calcular_velocidade(numero_voltas, extensao, tempo):
    distancia_km = (numero_voltas * extensao) / 1000
    tempo_horas = tempo / 60
    velocidade = distancia_km / tempo_horas

    print(f"Velocidade média: {velocidade} km/h")


def main():
    numero_voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite o tempo em minutos: "))

    calcular_velocidade(numero_voltas, extensao, tempo)


main()