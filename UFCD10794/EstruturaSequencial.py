import math

#1
print("Alo mundo")

#2
print("--" * 30)
numero = input("Digite um número: ")
print(numero)

#3
print("--" * 30)
numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))

print(f"A soma é {numero1 + numero2}")

#4
print("--" * 30)
media = 0
for x in range(4):
    media += float(input(f"Digite a nota {x + 1}: "))

print(f"A média é {media/4:.2f}")

#5
print("--" * 30)
medida = float(input("Digite a medida em metros: "))
print(f"Medida: {medida*100:.2f}cm")

#6
print("--" * 30)
raio = float(input("Digite o raio do círculo: "))
areaCirc = math.pow(raio,2) * math.pi
print(f"A área de circunferência é {round(areaCirc, 2)}")

#7
print("--" * 30)
lado = float(input("Digite a medida do lado do quadrado: "))
areaQuad = math.pow(lado, 2)
print(f"O dobro da área do quadrado é {areaQuad*2:.2f}")

#8
print("--" * 30)
valorHora = float(input("Digite o valor da hora trabalhada: "))
horaTrabalhada = float(input("Digite quantas horas foram trabalhadas neste mês: "))
print(f"Seu salário será {valorHora * horaTrabalhada:.2f} no mês corrente")

#9
print("--" * 30)
grausFahren = float(input("Digite a temperatura em graus Fahrenheit: "))
grausCels = 5 * ((grausFahren - 32) / 9)
print(f"São {grausCels:.2f}º Celsius de temperatura")

#10
print("--" * 30)
grausCels = float(input("Digite a temperatura em graus Celsius: "))
grausFahren = grausCels * 1.8 + 32
print(f"São {grausFahren:.2f}º Celsius de temperatura")

#11
print("--" * 30)
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = float(input("Digite um número real: "))

print(f"Cálculo letra a: {(num1*2) * (num2/2)}")
print(f"Cálculo letra b: {(num1*3) + num3}")
print(f"Cálculo letra c: {(math.pow(num3, 3))}")

#12
print("--" * 30)
altura = float(input("Digite a altura: "))
print(f"Seu peso ideal: {(72.7 * altura) - 58:.2f}kg")

#13
print("--" * 30)
altura = float(input("Digite a altura: "))
print(f"Peso ideal\nHomem: {(72.7 * altura) - 58:.2f}\nMulher: {(62.1 * altura) - 44.7:.2f}")

#14
print("--" * 30)
peso = float(input("Digite o total de peso pescado: "))
excesso = peso - 50.00
if excesso > 0:
    multa = excesso * 4.00
    print(f"Peso total: {peso:.2f}kg\nPeso excedente: {excesso:.2f}kg\nMulta: {multa:0.2f}€")
else:
    print(f"Peso total: {peso:.2f}kg\n\tNão excede o limite regulamentado")

#15
print("--" * 30)
valorHora = float(input("Digite o valor da hora trabalhada: "))
horaTrabalhada = float(input("Digite quantas horas foram trabalhadas neste mês: "))
ordenado = valorHora * horaTrabalhada

print(f"\t+ Salário Bruto: {ordenado:.2f}€\n\t- IR (11%): {ordenado * 0.11:.2f}€\n\t- INSS (8%): {ordenado * 0.08:.2f}€\n\t- Sindicato (5%): {ordenado * 0.05:.2f}€\n\t= Salário Líquido: {ordenado - ((ordenado * 0.11) + (ordenado * 0.08) + (ordenado * 0.05)):.2f}€")

#16
print("--" * 30)
areaPintura = float(input("Digite a área a ser pintada: "))
quantLatas = (areaPintura/3)/18
if  0 < quantLatas < 1:
    quantLatas = 1
print(f"\tQuantidade de latas: {round(quantLatas)}\n\tValor total: {quantLatas * 80.00:.2f}€")

#17
print("--" * 30)
areaPintura = float(input("Digite a área a ser pintada: "))
quantLitros = round(areaPintura/6, 2)
quantLatas = 0
quantGaloes = 0
while quantLitros > 0:
    if quantLitros >= 18:
        quantLatas += 1
        quantLitros -= 18
    elif 0 < quantLitros < 18:
        quantGaloes += 1
        quantLitros -= 3.6

if quantLatas > 0 and quantGaloes > 0:
    print(f"\tComprar {quantLatas} latas de 18l e {quantGaloes} galões de 3.6l")
elif quantLatas > 0 and quantGaloes == 0:
    print(f"\tComprar {quantLatas} latas de 18l")
else:
    print(f"\tComprar {quantGaloes} galões de 3.6l")

#18
print("--" * 30)
tamanhoFich = float(input("Digite o tamanho do ficheiro: "))
taxaVel = float(input("Digite a velicidade da internet: "))

print(f"Tempo aproximado de download: {tamanhoFich / taxaVel:.2f}s ")
