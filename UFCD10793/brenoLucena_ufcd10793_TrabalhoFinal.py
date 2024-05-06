inputFile = open("input-Notas.txt")
outputFile = open("pauta.txt", "w")

def Separadores(linhas):
    if(linhas):
        print("Nome        Apelido      Idade         Nota1        Nota2        Nota3        Nota4        Media        Resultado        Aproveitamento")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        outputFile.write("Nome        Apelido    Idade       Nota1       Nota2       Nota3       Nota4        Media       Resultado        Aproveitamento\n")
        outputFile.write("-------------------------------------------------------------------------------------------------------------------------------\n")
    else:
        print("Nome        Apelido      Idade         Nota1        Nota2        Nota3        Nota4        Media        Resultado        Aproveitamento")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
def Imprime(dados):
    for count in range(0, 7):
        print(f"{dados[count]:<8}", end=" ")
        print("   ", end=" ")
        outputFile.write(f"{dados[count]:<12}")

def CalcMedia(dados):
    media = 0
    quant = 0
    for count in range(3, 7):
        media += float(dados[count])
        quant += 1
    media /= quant
    print(f"{round(media, 2):<8}", end=" ")
    outputFile.write(f"{round(media, 2):<12}")
    if media >= 10:
        print(format("Aprovado", "^18"), end=" ")
        outputFile.write(f"{'Aprovado':^10}")
    else:
        print(f"{'Reprovado':^18}", end=" ")
        outputFile.write(f"{'Reprovado':^10}")

    return media

def Aproveitamento(media):
    if media < 5:
        print(f"{'Mau':^18}")
        outputFile.write(f"{'Mau':^28}")
    elif media < 10:
        print(f"{'Ins':^18}")
        outputFile.write(f"{'Ins':^28}")
    elif media < 15:
        print(f"{'Suf':^18}")
        outputFile.write(f"{'Suf':^28}")
    elif media < 18:
        print(f"{'Bom':^18}")
        outputFile.write(f"{'Bom':^28}")
    else:
        print(f"{'Muito Bom':^18}")
        outputFile.write(f"{'Muito Bom':^28}")
    outputFile.write("\n")

linhas = True
Separadores(linhas)
while linhas:
    leituraLinha = inputFile.readline()
    if not leituraLinha:
        linhas = False
    else:
        dados = leituraLinha.split()
        media = 0
        Imprime(dados)
        media = round(CalcMedia(dados), 2)
        Aproveitamento(media)

opcao = input("Deseja inserir algum cadastro? (s/n)")
opcao.lower()
while opcao != 's' and opcao != 'n':
    opcao = input("opção inválida! Escolha 's' para sim ou 'n' para encerrar o programa...")
if opcao == 's':
    while opcao == 's':
        dados[0] = input("Digite o nome do aluno: ")
        dados[1] = input("Digite o apelido do aluno: ")
        dados[2] = input("Digite a idade do aluno: ")
        dados[3] = input("Digite a nota 1 do aluno: ")
        dados[4] = input("Digite a nota 2 do aluno: ")
        dados[5] = input("Digite a nota 3 do aluno: ")
        dados[6] = input("Digite a nota 4 do aluno: ")
        Separadores(linhas)
        Imprime(dados)
        media = round(CalcMedia(dados), 2)
        Aproveitamento(media)
        opcao = input("Deseja inserir um novo cadastro? (s/n)")
        opcao.lower()
        while opcao != 's' and opcao != 'n':
            opcao = input("opção inválida! Escolha 's' para sim ou 'n' para encerrar o programa...")
    print("\nPrograma finalizado. Adeus...")
else:
    print("\nPrograma finalizado. Adeus...")