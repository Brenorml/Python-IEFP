#FUNÇÕES

def nome(nome: str):
    return nome.upper()

print(nome("Breno"))

def nome2(nome: str, idade: int) -> str:
    return f"O {nome} tem {idade} anos"

print(nome2("Breno", 41))

print(nome2(idade=20, nome="Carlos"))

def nome3(nome : str) -> str:
    if type(nome) == str:
        return nome.upper()
    else:
        print(f"tipo de dado errado {type(nome)} em vez de {str}")

print(nome3(1234))

def nome4(nome : str) -> str:
    try:
        return nome.upper()
    except AttributeError:
        print(f"tipo de dado errado {type(nome)} em vez de {str}")

print(nome4(1234))

def nome5(nome : str) -> str:
    try:
        return nome.upper()
    except AttributeError:
        print(f"tipo de dado errado {type(nome)} em vez de {str}")
    except KeyError:
        print(f"tipo de dado errado ")

print(nome5(''))

#LISTAS (ARRAYS)
listaNomes = ["Joao", "Maria", "Rita"]

print(listaNomes[2])
try:
    print(listaNomes[7])
except:
    print("o index não existe")

listaNomes.append("doidao")
print(listaNomes)
listaNomes.pop()
print(listaNomes)
listaNomes.pop(1)
print(listaNomes)

listaNomes2 = ["Joao", "Maria", "Rita", "Breno", "Diego", "Diogo", "Carlos", "Igor", "Paulo", "Bilbo", "Zion", "Bauer",
               "Ana", "Paula", "jack"]

print(listaNomes2[:5])
print(listaNomes2[2:5])
print(listaNomes2[5:15:5])

listaNomes2.remove("Maria")

print(listaNomes2[:5])

print("--" * 30)

for nomes in listaNomes2:
    print(nomes)

print("--" * 30)

for nomes in range(len(listaNomes2)):
    print(nomes)

print("--" * 30)

for i in range(listaNomes2.__len__()):
    print(listaNomes2[i])

print("--" * 30)

nova_lista = [n.upper() for n in listaNomes2]
print(nova_lista)

print("--" * 30)

nova_lista = [n.isnumeric() for n in listaNomes2]
print(nova_lista)

print("--" * 30)

nova_lista2 = [n for n in listaNomes2]
print(nova_lista2)

print("--" * 30)

nova_lista2 = [n.__len__() for n in listaNomes2 if n[-1] == "a"]
print(nova_lista2)

print("--" * 30)

listaNomes2.sort()
print(listaNomes2)

print("--" * 30)

listaNomes2.sort(reverse=True)
print(listaNomes2)

print("--" * 30)
#DICTIONARIES

aluno = {
    "nome": "Breno",
    "idade": 41,
    "Curso": "Programação"
}
print(aluno)

aluno["turma"] = "PROG13"
print(aluno)

print(aluno["nome"])

aluno.pop("idade")
print(aluno)

del aluno["Curso"]
print(aluno)

print("--" * 30)

for d in aluno: #imprime as keys por defeito
    print(d)

print("--" * 30)

for d in aluno.values(): #imprime os valores
    print(d)

print("--" * 30)

for d in aluno:
    print(aluno[d])

def teste(*nomes: str) -> str:
    print(nomes)

teste("Joao", "Rui", "Rita")

print("--" * 30)

def teste2(nomes: str, *notas: float):
    print(nomes)
    print([n for n in notas if n < 15])

teste2("Joao", 10, 20, 12, 12, 12, 10, 2, 5)

print("--" * 30)

def teste3(nomes: str, **notas):
    print(f"{nomes} tem {notas['nota']} na UFCD {notas['ufcd']}")


teste3("Joao", nota = 10, ufcd = 10794)

print("--" * 30)

def teste4(nomes: str, nota: float = 0):
    print(f"{nomes} teve {nota} valores")


teste4("Mario")
teste4("Rui", 13)