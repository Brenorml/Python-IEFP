from datetime import date
#classes

def OlaMundo1():
    pass

def OlaMundo2():
    pass

class Morada:
    def __init__(self, rua: str):
        self.rua = rua
class Pessoa: #No momento que um constructor é feito não há necessidade de manter declaração de propriedades nome, idade e email
    nome: str
    idade: int
    email: str

    def __init__(self, nome: str, idade: int, email: str, rua: Morada): #contructor
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = 12345678
        self.morada = Morada("Rua x")

    def growup(self):
        self.idade += 1

    def ano_nascimento(self):
        ano = date.today().year
        anoNascimento = ano - self.idade
        #return f"It works!! {self.nome}"
        return anoNascimento

    def get_info(self):
        return f"nome: {self.nome}, idade: {self.idade}"



