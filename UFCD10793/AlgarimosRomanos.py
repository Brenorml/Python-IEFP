num = int(input("Inserir o numero: "))
# print("valor:", num)
numRoman = ""

if 0 < num <= 3999:
    while num >= 1000:
        numRoman += "M"
        num -= 1000

    print(num)

    while num >= 100:
        if num >= 900:
            numRoman += "CM"
            num -= 900
        elif 500 <= num < 900:
            numRoman += "D"
            while num >= 600:
                numRoman += "C"
                num -= 100
            num -= 500
        elif 100 <= num < 400:
            while num >= 100:
                numRoman += "C"
                num -= 100
        else:
            numRoman += "CD"
            num -= 400


    print(num)

    while num >= 90:
        numRoman += "XC"
        if num == 99:
            numRoman += "IX"
            num -= 9
        elif 95 <= num < 99:
            numRoman += "V"
            while num > 95:
                numRoman += "I"
                num -= 1
            num -= 5
        elif num == 94:
            numRoman += "IV"
            num -= 4
        elif 90 < num < 94:
            numRoman += "I"
            num -= 1
        num -= 90

    while num >= 10:
        if num >= 50:
            numRoman += "L"
            while num >= 60:
                numRoman += "X"
                num -= 10
            num -= 50
        elif 10 <= num < 40:
            while num >= 10:
                numRoman += "X"
                num -= 10

        else:
            numRoman += "XL"
            num -= 40

    print(num)

    while(num >= 1):
        if 5 <= num < 9 :
            numRoman += "V"
            while num > 5:
                numRoman += "I"
                num -= 1
            num -= 5
        elif num == 4:
            numRoman += "IV"
            num -= 4
        elif num < 4:
            while num > 0:
                numRoman += "I"
                num -= 1
        else:
            numRoman += "IX"
            num -= 4

    print(numRoman)
    print(num)
elif num == 0:
    print("Error: Número não existe")
else:
    print("Error: O número limite é 3999")
