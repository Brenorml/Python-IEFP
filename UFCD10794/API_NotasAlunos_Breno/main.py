from fastapi import FastAPI
import sqlite3
from SQL_handler import SQL_handler
from model import Alunos

app = FastAPI()

@app.get("/")
async def root():
    return {"Aluno: Breno Lucena | Turma: NST-Prog13"}

#configuração do DB - tabelas
@app.get("/setup")
async def Setup():
    conn = sqlite3.connect('estudantes.db')
    cur = conn.cursor()

    table = """ CREATE TABLE aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255),
                idade INTERGER,
                notas_aluno INTEGER,
                FOREIGN KEY (notas_aluno) REFERENCES nota(id)
                );
                """
    cur.execute(table)

    table = """ CREATE TABLE nota(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nota1 REAL,
                nota2 REAL,
                nota3 REAL,
                nota4 REAL
                );
                """
    cur.execute(table)

    table = """ CREATE TABLE pauta(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255),
                apelido VARCHAR(255),
                idade INTERGER,
                nota1 REAL,
                nota2 REAL,
                nota3 REAL,
                nota4 REAL,
                media REAL,
                resultado VARCHAR(255),
                aproveitamento VARCHAR(255)                
                );
                """
    cur.execute(table)
    conn.commit()
    conn.close()

    return "Configuração criada com sucesso!!!"

#configuração do DB - popular tabelas com dados não processados
@app.get("/inserirdados")
async def InsertData():
    query = """INSERT INTO aluno (nome, idade, notas_aluno) VALUES 
    ('João Silva', 20, 1),
    ('Maria Santos', 22, 2),
    ('Pedro Oliveira', 21, 3),
    ('Ana Martins', 19, 4),
    ('Carlos Souza', 23, 5),
    ('Mariana Silva', 20, 1),
    ('Lucas Santos', 21, 2),
    ('Juliana Oliveira', 22, 3),
    ('Fernando Martins', 19, 4),
    ('Camila Souza', 24, 5),
    ('Rafael Silva', 20, 1),
    ('Isabela Santos', 21, 2),
    ('Felipe Oliveira', 22, 3),
    ('Patrícia Martins', 19, 4),
    ('Gabriel Souza', 23, 5);
    """
    SQL_handler.update_data(query)

    query = """INSERT INTO nota (nota1, nota2, nota3, nota4) VALUES
    (12.3, 8.7, 15.5, 6.8),
    (20.0, 13.2, 11.1, 18.6),
    (5.7, 4.4, 3.9, 2.2),
    (17.9, 4.6, 9.0, 14.3),
    (10.2, 19.1, 8.4, 11.7),
    (6.5, 14.8, 10.3, 7.0),
    (13.6, 8.1, 18.7, 2.9),
    (16.0, 11.4, 19.8, 5.3),
    (7.4, 17.2, 12.9, 8.5),
    (0.5, 9.5, 6.6, 16.1),
    (18.3, 5.9, 13.4, 10.8),
    (8.9, 12.7, 17.6, 4.1),
    (19.7, 15.2, 18.6, 20.0),
    (11.3, 18.0, 4.8, 12.4),
    (6.0, 13.9, 11.2, 7.6);

    """
    SQL_handler.update_data(query)

    return "Dados inseridos com sucesso"

#configuração do DB - buscar dados nas tabelas aluno e nota e popular dados na tabela destino
@app.get("/pauta/base")
async def AddData():
    query = """SELECT aluno.nome, aluno.idade, nota.* FROM aluno
               JOIN nota ON aluno.notas_aluno = nota.id;"""
    list = SQL_handler.select_data(query)

    for item in list:
        # slit do dado nome advindo da table aluno para atribuição na coluna nome e apelido da tabela pauta
        splitName = item[0].split()
        firstname = splitName[0]
        secondname = splitName[1]

        #verifica se existe sobrenome com a função len para direcionar o comando correcto
        if len(splitName) >= 2:
            query = f"""INSERT INTO pauta (nome, apelido, idade, nota1, nota2, nota3, nota4) VALUES
                        ('{firstname}', '{secondname}', {item[1]}, {item[3]}, {item[4]}, {item[5]}, {item[6]});"""
            SQL_handler.update_data(query)
        else:
            query = f"""INSERT INTO pauta (nome, idade, nota1, nota2, nota3, nota4) VALUES
                        ('{item[0]}', {item[1]}, {item[3]}, {item[4]}, {item[5]}, {item[6]});"""
            SQL_handler.update_data(query)

    return "Dados inseridos com sucesso"

#processamento dos dados das tabelas origem e inserção de dados na tabela destino (pauta)
#configuração do DB - calcular as medias e inserir na tabela pauta
@app.get("/pauta/media")
async def CalcMedia():
    query = """SELECT nota1, nota2, nota3, nota4 FROM pauta;"""
    list = SQL_handler.select_data(query)
    count = 1
    for item in list:
        query = f"""UPDATE pauta SET media = ROUND(({item[0]} + {item[1]} + {item[2]} + {item[3]}) / 4, 2) 
                    WHERE id = {count};"""
        count += 1
        SQL_handler.update_data(query)
    return "Medias calculadas com sucesso."

#configuração do DB - verificar resultado e inserir na tabela pauta
@app.get("/pauta/resultado")
async def VerifyResult():
    query = """SELECT media FROM pauta;"""
    list = SQL_handler.select_data(query)
    count = 1

    for item in list:
        if item[0] >= 10:
            result = "aprovado"
        else:
            result = "reprovado"

        query = f"""UPDATE pauta SET resultado = '{result}' WHERE id = {count};"""
        count += 1
        SQL_handler.update_data(query)

    return "Resultados adicionados com sucesso."

#configuração do DB - verificar aproveitamento e inserir na tabela pauta
@app.get("/pauta/aproveitamento")
async def VerifyPerform():
    query = """SELECT media FROM pauta;"""
    list = SQL_handler.select_data(query)
    count = 1

    for item in list:
        avarage = int(item[0])
        if avarage < 5:
            perform = "mau"
        elif avarage < 10:
            perform = "insuficiente"
        elif avarage < 15:
            perform = "suficiente"
        elif avarage < 18:
            perform = "bom"
        else:
            perform = "muito bom"

        query = f"""UPDATE pauta SET aproveitamento = '{perform}' WHERE id = {count};"""
        count += 1
        SQL_handler.update_data(query)
    return "Performance adicionada com sucesso"

#lista todos os alunos da tabela pauta
@app.get("/alunos")
async def GetStudentFull():
    query = """SELECT * FROM pauta;"""
    alunosbase = SQL_handler.select_data(query)
    msg = []
    for item in alunosbase:
        msg.append({f"ID": item[0], f"nome": item[1], f"apelido": item[2], f"idade": item[3], f"nota1": item[4], \
                    f"nota2": item[5], f"nota3": item[6], f"nota4": item[7], f"media": item[8], f"resultado": item[9], \
                    f"aproveitamento": item[10]})
    return msg

#busca paginada de alunos e seus resultados
@app.get("/alunos")
async def GetStudent(pag: int, num: int):
    query = """SELECT * FROM pauta"""
    alunos = SQL_handler.select_data(query)

    msg = []

    lb = (pag - 1) * num  # 1º index da página
    up = lb + num  # ultimo index da numero + 1

    if up >= len(alunos):
        up = len(alunos)

    if lb > len(alunos):
        return msg

    for i in range(lb, up):
        msg.append(
            {f"nome": alunos[i][1] + ' ' + alunos[i][2],
             f"media": alunos[i][8],
             f"resultado": alunos[i][9]
             }
        )
    return msg

#insere novo aluno na tabela pauta
@app.post("/alunos")
async def PostStudent(aluno: Alunos):
    aluno.AddToDB()
    return f"{aluno.nome} {aluno.apelido} salvo na base de dados"

#atualiza aluno na tabela pauta
@app.put("/alunos")
async def PutStudent(aluno: Alunos):
    msg = aluno.UpdateDB()
    return msg

#lista alunos conforme resultado
@app.get("/alunos/{resultado}")
async def GetStudentByResult(resultado: str):
    query = f"""SELECT nome, apelido, aproveitamento FROM pauta WHERE resultado = '{resultado}';"""
    alunos = SQL_handler.select_data(query)

    msg = []
    for aluno in alunos:
        msg.append({f"nome": aluno[0], f"apelido": aluno[1], f"aproveitamento": aluno[2]})
    return msg

#lista alunos conforme resultado e aproveitamento
@app.get("/{resultado}/alunos/{performance}")
async def GetStudentByResult(resultado: str, performance: str):
    query = f"""SELECT nome, apelido FROM pauta WHERE resultado = '{resultado}' AND aproveitamento = '{performance}';"""
    alunos = SQL_handler.select_data(query)

    msg = []
    for aluno in alunos:
        msg.append({f"nome": aluno[0], f"apelido": aluno[1]})
    return msg

#lista alunos editados na tabela pauta comparando tabelas pauta vs aluno + nota
@app.get("/listaeditada")
async def GetStudentEdited():
    query = """SELECT aluno.nome, aluno.idade, nota.nota1, nota.nota2, nota.nota3, nota.nota4 FROM aluno JOIN nota ON 
               aluno.notas_aluno = nota.id;"""
    alunos_base = SQL_handler.select_data(query)
    query = """SELECT nome, apelido, idade, nota1, nota2, nota3, nota4 FROM pauta;"""
    alunos_pauta = SQL_handler.select_data(query)

    lista_base = []
    # atribuição de valores a lista_base para tratamento de dados (split do nome e apelido do index[0])
    for aluno in alunos_base:
        nomecompleto = aluno[0].split()
        nome = nomecompleto[0]
        apelido = nomecompleto[1]
        lista_base.append({f"nome": nome, f"apelido": apelido, f"idade": aluno[1], f"nota1": aluno[2], \
                       f"nota2": aluno[3], f"nota3": aluno[4], f"nota4": aluno[5]})
    lista_pauta = []
    for aluno in alunos_pauta:
        lista_pauta.append({f"nome": aluno[0], f"apelido": aluno[1], f"idade": aluno[2], f"nota1": aluno[3], \
                       f"nota2": aluno[4], f"nota3": aluno[5], f"nota4": aluno[6]})

    msg = []

    # vifica mudança nos elementos adicionados das tabelas aluno e nome para a tabela pauta
    for i in range(min(len(lista_base), len(lista_pauta))):
        if lista_base[i] != lista_pauta[i]:
            msg.append(lista_pauta[i])

    # indica qual o item adicionado apos a passagem dos dados entre tabelas
    for i in range(len(lista_base), len(lista_pauta)):
        msg.append(lista_pauta[i])

    return msg



