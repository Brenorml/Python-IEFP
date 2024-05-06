from fastapi import FastAPI
import sqlite3
from SQL_handler import SQL_handler
from model import Jogador, Equipa

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/setup")
async def setup():
    conn = sqlite3.connect('jogadores.db')
    cur = conn.cursor()

    table = """ CREATE TABLE jogador (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome VARCHAR(255) NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            pos VARCHAR(255) NOT NULL,
            classif REAL NOT NULL,
            equipa INTEGER NOT NULL, 
            FOREIGN KEY (equipa) REFERENCES clube(id)
            );
            """
    cur.execute(table)

    table = """ CREATE TABLE clube(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome VARCHAR(255) NOT NULL,
            estadio VARCHAR(255) NOT NULL,
            cidade VARCHAR(255) NOT NULL,
            abrev VARCHAR(255) NOT NULL,
            ano INTEGER NOT NULL
            );
            """

    cur.execute(table)
    conn.commit()
    conn.close()

    return "Configuração criada com sucesso!!!"

@app.get("/setupData")
async def InsertData():
    query = """INSERT INTO clube (nome, estadio, cidade, abrev, ano) VALUES
    ('Manchester United', 'Old Trafford', 'Manchester', 'MUN', 1878),
    ('Paris Saint-Germain', 'Parc des Princes', 'Paris', 'PSG', 1970),
    ('Bayern Munich', 'Allianz Arena', 'Munich', 'FCB', 1900),
    ('Manchester City', 'Etihad Stadium', 'Manchester', 'MCI', 1880),
    ('Liverpool', 'Anfield', 'Liverpool', 'LIV', 1892),
    ('Real Madrid', 'Santiago Bernabéu', 'Madrid', 'RMA', 1902),
    ('FC Barcelona', 'Camp Nou', 'Barcelona', 'BAR', 1899),
    ('Juventus', 'Allianz Stadium', 'Turin', 'JUV', 1897),
    ('Chelsea', 'Stamford Bridge', 'London', 'CHE', 1905),
    ('AC Milan', 'San Siro', 'Milan', 'ACM', 1899);
    """
    SQL_handler.update_data(query)

    query = """INSERT INTO jogador (nome, peso, altura, pos, classif, equipa) VALUES
    ('Cristiano Ronaldo', 80.5, 1.87, 'Atacante', 90.5, 1),
    ('Lionel Messi', 72.3, 1.70, 'Atacante', 92.0, 7),
    ('Neymar Jr', 68.0, 1.75, 'Atacante', 88.5, 2),
    ('Robert Lewandowski', 81.0, 1.84, 'Atacante', 89.7, 3),
    ('Kevin De Bruyne', 70.2, 1.81, 'Meio-campista', 87.5, 4),
    ('Virgil van Dijk', 92.0, 1.93, 'Zagueiro', 88.2, 5),
    ('Kylian Mbappé', 73.0, 1.78, 'Atacante', 91.0, 2),
    ('Sergio Ramos', 82.5, 1.84, 'Zagueiro', 86.8, 6),
    ('Luka Modrić', 68.8, 1.72, 'Meio-campista', 89.5, 7),
    ('Erling Haaland', 88.0, 1.94, 'Atacante', 87.7, 3);
    """
    SQL_handler.update_data(query)

    return "Data inserido com sucesso"

@app.get("/clubs")
async def GetClubs(pag: int, num: int):
    conn = sqlite3.connect('jogadores.db')
    cur = conn.cursor()
    query = """SELECT * FROM clube"""
    lista = cur.execute(query)
    clubes = lista.fetchall()
    conn.close()

    msg = []

    lb = (pag - 1) * num  # 1º index da página
    up = lb + num  # ultimo index da numero + 1

    if up >= len(clubes):
        up = len(clubes)

    if lb > len(clubes):
        return msg

    for i in range(lb, up):
        msg.append(
            {f"nome": clubes[i][1],
             f"abrev": clubes[i][4]
             }
        )
    return msg

@app.post("/clubs")
async def PostClubs(clube: Equipa):
    clube.AddToDB()
    return f"{clube.nome} salvo na base de dados"

@app.put("/clubs")
async def PutClubs(clube: Equipa):
    msg = clube.UpdateDB()
    return msg

@app.get("/clube/{abrev}/players")
async def GetClubs(abrev: str):
    conn = sqlite3.connect('jogadores.db')
    cur = conn.cursor()
    table = f"""SELECT jogador.*, clube.abrev FROM jogador JOIN
        clube ON jogador.equipa = clube.id WHERE clube.abrev = '{abrev}';"""
    lista = cur.execute(table)
    players = lista.fetchall()
    conn.close()

    msg = []
    for player in players:
        msg.append({f"nome": player[1], f"pos": player[4]})
    return msg

@app.post("/clube/{abrev}/players")
async def PostClubs(abrev: str, nome_jogador: str):
    table = f"""UPDATE clube SET abrev = '{abrev}' WHERE id IN 
                (SELECT equipa FROM jogador WHERE nome = '{nome_jogador}');"""
    print(table)
    return SQL_handler.update_data(table)

@app.get("/clube/{abrev}/players/{pos}")
async def GetClubs(abrev: str, pos: str):
    table = f"""SELECT jogador.*, clube.abrev FROM jogador JOIN
        clube ON jogador.equipa = clube.id WHERE clube.abrev = '{abrev}' AND 
        jogador.pos = '{pos}';"""
    players = SQL_handler.select_data(table)

    msg = []
    for player in players:
        msg.append({f"nome": player[1], f"pos": player[7]})
    return msg

@app.get("/player")
async def GetPlayers(pag: int = 1, num: int = 10):
    conn = sqlite3.connect('jogadores.db')
    cur = conn.cursor()
    query = """SELECT * FROM jogador"""
    lista = cur.execute(query)
    jogadores = lista.fetchall()
    conn.close()

    msg = []

    lb = (pag - 1) * num  # 1º index da página
    up = lb + num  # ultimo index da numero + 1

    if up >= len(jogadores):
        up = len(jogadores)

    if lb > len(jogadores):
        return msg

    for i in range(lb, up):
        msg.append({f"nome {i}": jogadores[i][1]})
    return msg

@app.post("/player")
async def PostPlayer(jogador: Jogador):
    jogador.AddToDB()
    return f"{jogador.nome} salvo na base de dados"

@app.put("/player")
async def PutPlayer(jogador: Jogador):
    msg = jogador.UpdateDB()
    return msg