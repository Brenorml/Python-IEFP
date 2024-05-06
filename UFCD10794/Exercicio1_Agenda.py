class CadastroAgenda:
    def __init__(self, id, nome, contacto, endereco, email):
        self.id = id
        self.nome = nome
        self.contacto = contacto
        self.endereco = endereco
        self.email = email

opcao = 's'
i = 0
listaContatos = []
print("Agenda de Contactos")
print("-------------------")
while opcao == 's':
    id = i + 1
    nome = input("Insira o nome: ")
    contacto = input("Insira o contacto: ")
    endereco = input("Insira o endereço: ")
    email = input("Insira o email: ")
    listaContatos.append(CadastroAgenda(id, nome, contacto, endereco, email))
    i += 1
    opcao = input("Deseja inserir outro contacto? (s/n)")
    while opcao != 's' and opcao != 'n':
        opcao = input("Opcao invalida. Digite 's' para sim ou 'n' para encerrar o aplicativo...")

for listaContatos in listaContatos:
    print("ID: ", listaContatos.id, "\n", "Nome: ", listaContatos.nome, "\n", "Contacto: ", listaContatos.contacto, "\n", "Endereço: ", listaContatos.endereco , "\n", "Email: ", listaContatos.email, "\n")
