t=(1,2,3)
print(t)
for i in range(len(t)):
    print(t[i], end=' ')
print()
lista = list(t)
print(lista)
lista[1] = 6
t=tuple(lista)
print(t)

dic={'joão':100, 'maria':150}
print(dic['joão'])
print(dic)
print(dic['maria'])
dic['pedro'] = 10
print(dic['pedro'])
print(dic)
dic['breno'] = 200
print(dic)
dic['patricia'] = 50
print(dic['patricia'])
print(dic)
d=dict([(1,2), ('chave', 'conteudo')])
print('valor da chave 1 =', d[1])
print('valor da "chave ="', d['chave'])
d[2]='conteudo'
print('valor da chave 2 =', d[2])
print(d)
d2=dict(x=1, y=2, nome='Luisa')
print(d2)
print('valor da chave x =', d2['x'])
print('valor da chave y =', d2["y"])
print('valor da chave nome =', d2["nome"])
x={'a': 'João', 'b':'Maria'}
print(x)
y = x
print(y)
# x.clear()
print(x)
print(y)
x['c'] = 'Luisa'
print('x=', x, 'y=', y)
y['a'] = 'Fernando'
print('x=', x, 'y=', y)
x = {}
print('x=', x, 'y=', y)
w={'João':[14,12], 'Maria':[13,14]}
z=w.copy()
print(w)
print(z)
z['Pedro'] = [15,16]
w['João'] += [13]
print(w)
print(z)