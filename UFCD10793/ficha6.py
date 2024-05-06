lista = []
print(lista)
lista = [1, 'a', 2+3j, ['ab', 'CD']]
print(lista[0])
print(lista[2])
print(lista[3])
print(lista[-1])
lista[0] = 2
print(lista)
lista1 = [0]*4
print(lista1)
lista1 = lista1+[1]*3
print(lista1)
lista2 = [1, 2, 3, ['ab', 'CD']]
print(lista2)
del lista2[2]
print(lista2)
del lista2[2][1]
print(lista2)
lista3 = [1, 'a', 2+3j, ['ab', 'CD']]
print(lista3[0:])
print(lista3[0:-1])
print('lista3[:1]->', lista3[:1])
print('lista3[1:2]->', lista3[1:2])
print('lista3[3][0]->', lista3[3][0])
print('lista3[3][0:]->', lista3[3][0:])
lista4 = [1, 'y', ['ab', 'CD']]
print(lista4)
lista4[1:1] = ['z']
print(lista4)
lista4[1:3] = ['x']
print(lista4)
lista4[1:-1] = [2,3,4]
print(lista4)
lista4[2:2] = ['xyz']
print(lista4)
# print(lista4)
lista5=[1,2,3,4,5]
print(lista5)
print(lista5[0:2])
print(lista5[5:0:-1])
print(lista5[5:-1])
# 16= ['a',2,3,'d','x']
print(16)
print(16[:3:2])
print(16[::-1])
print(16[0::2])
16[0::2]=[6,7,8]
print(16)
# 17=[1, 'a', 'bc']
print(17)
print('1 pertence à 17?', 1 in 17)
print('2 pertence à 17?', 2 in 17)
print('b pertence à 17?', 'b' in 17)
print('b pertence à 17[2?', 'b' in 17)
print("'bc' pertence à 'abcd'", 'bc' in 'abcd')
# 18=[]
print(18)
# 18=[0]*10
print(18)
18[0]=3
print(18)
# 18=[None]*5
print(18)
18[3]=6
print(18)