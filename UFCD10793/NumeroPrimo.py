num = int(input("Insira um número inteiro positivo: "))
i = num
count = 0
aux = 0

if num > 1:
    while i > 1:
        if num % i == 0:
            aux = i
            count += 1
        i -= 1
    if count > 1:
        print(num, "é mútiplo de", aux)
    else:
        print(num, "é primo")
elif num == 1:
    print("1 não é primo")
else:
    print("0 não é primo")


