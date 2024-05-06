l1 = [1,2,3]
l2 = ['a', 'b', 'c', 'd', 'e']
resultado = []
tamanhoMaximo = max(len(l1), len(l2))

for i in range(tamanhoMaximo):
    if i < len(l1):
        resultado.append(l1[i])
    if i < len(l2):
        resultado.append(l2[i])

print(resultado)

m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[10,11,12], [13,14,15], [16,17,18]]

if len(m1[0]) != len(m2):
    print("As matrizes devem ter as mesmas dimensões.")
else:
    produto = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            produto[i][j] += m1[i][k] * m2[k][j]

for linha in produto:
    print(linha)

