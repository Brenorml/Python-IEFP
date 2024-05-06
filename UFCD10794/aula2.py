s2 = """
        teste
        test1
        test2
"""
print(s2)

if 10 > 20:
    print("10 > 20")
else:
    print("10 <= 20")

n1 = 10
n2 = 9
n3 = 8
if n1 > n2:
    print(f"{n1:.2f} > {n2} teste")
elif n2 > n3:
    print(f"{n2:.2f} > {n3} teste")
else:
    print(f"{n3:.2f}")

match n1: #switch
    case 10:
        print("10")
    case 15:
        print("15")
    case _: #default
        print("outro valor")

print("--" * 10)
print(range(100_000_000_000_000_000_000, 7).__contains__(43)) #contains é um metodo para verificar se o parametro esta contido no range indicado, com saltos de 7 em 7
print("--" * 10)
print("fim")

