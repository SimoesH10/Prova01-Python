def q1():
    ano = int(input("Digite o ano da vacinação: "))
    intervalo = 4
    for i in range(1, 5):
        print(ano + i * intervalo, end=" ")


def q2():
    numeros = []
    while True:
        n = int(input("Digite um número (ou um valor negativo para encerrar): "))
        if n < 0:
            break
        numeros.append(n)
    for n in numeros:
        if n % 2 == 1:
            print("Primo")
        else:
            print("Não")

def q3():
    total = 0
    contador = 0
    while True:
        doacao = float(input("Digite o valor da doação (ou um valor negativo para encerrar): "))
        if doacao < 0:
            break
        total += doacao
        contador += 1
    print(f"{total:.2f}")
    if contador > 0:
        print(f"{(total / contador):.2f}")
    else:
        print("0.00")

def q4():
    km_rodado = int(input("Digite a quilometragem total rodada: "))
    dias = int(input("Digite a quantidade de dias de aluguel: "))

    if dias <= 0:
        print("Valor inválido")
        return

    valor_diaria = 90
    km_incluso = 100
    taxa_extra = 12

    total = dias * valor_diaria
    if km_rodado > dias * km_incluso:
        km_extra = km_rodado - dias * km_incluso
        total += km_extra * taxa_extra

    print(f"{total:.2f}")

def q5():
    escala = input("Digite a escala da temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
    try:
        temperatura = float(input("Digite o valor em números da temperatura: "))
    except ValueError:
        print("Valor inválido")
        return

    if escala == 'C':
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
        print(f"{fahrenheit:.2f} F")
        print(f"{kelvin:.2f} K")
    elif escala == 'F':
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{celsius:.2f} C")
        print(f"{kelvin:.2f} K")
    elif escala == 'K':
        if temperatura < 0:
            print("Valor de temperatura abaixo do minimo")
            return
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f} C")
        print(f"{fahrenheit:.2f} F")
    else:
        print("Escala inválida. Use C, F ou K.")
