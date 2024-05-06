#import aula4
from aula4 import OlaMundo2
from datetime import timezone
from datetime import date
from datetime import datetime
from aula4 import Pessoa
from aula4 import Morada

#OlaMundo1() - da erro pq foi importado apenas a função OlaMundo2()

OlaMundo2() #não precisa instanciar a modulo aula4.

print(timezone.max)
print(date.today())
print(datetime.now())

#p1 = Pessoa()
#A PARTIR DO MOMENTO QUE UM CONSTRUCTOR FOI ACRESCENTADO A PASSAGEM DE PARAMETROS É FEITA COMO NO CONSTRUCTOR EX: P2)
# p1.nome = "Breno"
# p1.idade = 40
# p1.email = "breno@pt.pt"
p1 = Pessoa("Breno", 34, "breno@test.pt")

print(p1.nome, p1.idade, p1.email)

p1.ano_nascimento()

p2 = Pessoa("Carla", 25, "carla@teste.pt")

print(p2.nome)

idade1 = p1.ano_nascimento()
idade2 = p2.ano_nascimento()
print(idade1)
print(idade2)

print("--" * 30)

print(p2.get_info())
p2.growup()
print(p2.get_info())


print(p1.morada.rua)