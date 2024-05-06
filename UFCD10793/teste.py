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