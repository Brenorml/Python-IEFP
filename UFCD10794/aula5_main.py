from aula5_class import Morada, Morada2, Morada3

morada = Morada("rua1", "12A", "Esq", 1245601)
print(morada) #Dataclasse imprime todos os dados

#morada2 = Morada2("rua2", "13A", "Esq", 987654321) #Falta o constructor, quando instanciado deu erro
#print(morada2)

morada3 = Morada3("rua2", "13A", "Esq", 987654321)
print(morada3) #imprime informações de localicação e objeto
print(morada3.rua, morada3.num, morada3.apt, morada3.cp)

print(morada.get_cp_formatado())