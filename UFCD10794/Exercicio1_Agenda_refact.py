class CadastroAgenda:
    def __init__(self, id, nome, contacto, endereco, email):
        self.id = id
        self.nome = nome
        self.contacto = contacto
        self.endereco = endereco
        self.email = email

def ListarContactos(listaContactos):
    if len(listaContactos) == 0:
        print("\nA lista está vazia.\n")
    else:
        for listaContatos in listaContactos:
            print("ID: ", listaContatos.id, "\n", "Nome: ", listaContatos.nome, "\n", "Contacto: ", listaContatos.contacto,
                "\n", "Endereço: ", listaContatos.endereco, "\n", "Email: ", listaContatos.email, "\n")

def AdicionarContacto(listaContactos):
    opcao = 's'
    i = 0
    while opcao == 's':
        id = i + 1
        nome = input("Insira o nome: ")
        contacto = input("Insira o contacto: ")
        endereco = input("Insira o endereço: ")
        email = input("Insira o email: ")
        listaContactos.append(CadastroAgenda(id, nome, contacto, endereco, email))
        i += 1
        opcao = input("Deseja inserir outro contacto? (s/n)")
        while opcao != 's' and opcao != 'n':
            opcao = input("Opcao invalida. Digite 's' para sim ou 'n' para encerrar o aplicativo...")
    print("\nContacto Inserido com sucesso!!!\n")

listaContactos = []
opcao = -1

while opcao != 0:
    print("Agenda    de    Contactos")
    print("-------------------------")
    opcao = int(input("Escolha:\n1 - Listar\n2 - Inserir cadastro\n0 - Sair\n"))
    if opcao == 1:
        ListarContactos(listaContactos)
    elif opcao == 2:
        AdicionarContacto(listaContactos)
    elif opcao < 0 or opcao > 2:
        print("Opção inválida!!!")
    else:
        print("Aplicação encerrada. Adeus...")