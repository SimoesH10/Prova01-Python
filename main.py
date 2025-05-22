def q1():
    ano = int(input("Digite o ano da vacinação: "))
    intervalo = 0

    for i in range(1, 4):
        print("Próxima dose em:", ano + i * intervalo)

def q2():
    numeros = []

    while True:
        n = int(input("Digite um número (ou um valor negativo para encerrar): "))
        if n <= -1:
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

    if contador > 0:
        media = total / contador
        print(f"Total arrecadado: R${total:.2f}")
        print(f"Valor médio das doações: R${media:.2f}")
    else:
        print("Nenhuma doação foi feita.")

def q4():
    dias = int(input("Digite a quantidade de dias de aluguel: "))
    km_rodado = int(input("Digite a quilometragem total rodada: "))

    valor_diaria = 90
    km_incluso = 100
    taxa_extra = 12

    total = dias * valor_diaria

    if km_rodado > dias * km_incluso:
        km_extra = km_rodado - dias * km_incluso
        total += km_extra * taxa_extra

    print(f"{total:.2f}")

def q5():
    escala = input("Digite a escala da temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
    temperatura = int(input("Digite o valor em números da temperatura: "))

    if escala == 'C':
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
        print(temperatura, fahrenheit, kelvin, )
    elif escala == 'F':
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15
        print(temperatura, celsius, kelvin)
    elif escala == 'K':
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(temperatura, celsius, fahrenheit)
    else:
        print("Escala inválida. Use C, F ou K.")

if __name__=="__main__":
    q2()