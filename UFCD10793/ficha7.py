lista=[1,2,9,3,4]
print('Tamanho da lista: ', len(lista))
print('Minimo da lista: ', min(lista))
print('Maximo da lista: ', max(lista))
print('Maximo da lista: ', max(['a','b','c']))
print('Maximo da lista: ', max(1,2,3,4))
print('Minimo da lista: ', min(1,2,3,4))

lista=list('alo')
print(lista)
print('Tipo da lista:', type(lista))
lista[1]='xx'
print(lista)
lista1=''.join(lista)
print('lista1:', lista1)
print('Tipo da lista1:', type(lista1))
lista2=''
lista2=lista2.join(lista)
print('lista2:', lista2)
print('Tipo da lista2:', type(lista2))

# range(inicio, fimExclusive, intervalo)
lista2=list(range(0,5))
print(lista2)
lista3=list(range(3))
print(lista3)
lista4=list(range(2,10,2))
print(lista4)
lista5=list(range(10,2,-3))
print(lista5)

# for variavel in lista/range
for elemento in range(1,7):
    print(elemento, end= ' ')
print()

lista5=list(range(10,2,-3))
print(lista5)
for elemento in lista5:
    print(elemento,end=' ')
print()

# comparação de listas
print('lista4 == lista5?', lista4 == lista5)
lista4=lista5
print('lista4 == lista5?', lista4 == lista5)
a=[1,2,3]
b=[3,1,2]
print('a == b?', a == b)
b.sort()
print(a)
print(b)
print('a == b?', a == b)
print([1,2] < [2,3])
a=[1,2]
b=[2,3]
print('a < b?', a < b)
print(min([[1], [2,3], [3,4], []]))
print(max([[1], [2,3], [3,4], []]))
# print(min(0,[],""))
# print(max(0,[],""))
print(type(a))

# variaveis do tipo list são referências (apontadores-endereços de memória)
a = b = [1,2,3] # declara duas listas iguais? Não! declara duas referências para a mesma lista
c = a           # atribui a c, uma rederência para a
d = c[:]        # atribui a d uma referência para c? não - atribui os elementos um a um
                # a uma nova lista apontada pelo conteudo d
e = c           # atribui a variavel e o conteudo de c que e o endereco da lista original
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('e:', e)
print('a is b:', a is b)        # tentar usar concatenação
print('c is a:', c is a)
print('c is b:', c is b)
print('d is c:', d is c)
print('e is c:', e is c)
a[1] = 5        # [1,5,3]
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)  # [1,2,3]
print('e:', e)
