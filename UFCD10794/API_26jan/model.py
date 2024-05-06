import sqlite3
from pydantic import BaseModel
from SQL_handler import SQL_handler

class Jogador(BaseModel):
    nome: str
    peso: float
    altura: float
    pos: str
    classif: float
    equipa: int

    def AddToDB(self):
        conn = sqlite3.connect('jogadores.db')
        cur = conn.cursor()
        query = f"""INSERT INTO jogador (nome, peso, altura, pos, classif, equipa) VALUES (            
            '{self.nome}',
            {self.peso},
            {self.altura},
            '{self.pos}',
            {self.classif},
            {self.equipa});"""

        print(query)

        cur.execute(query)
        conn.commit()
        conn.close()

    def UpdateDB(self):
        getData = f"""SELECT * FROM jogador WHERE nome = '{self.nome}'"""
        count =  SQL_handler.select_data(getData).__len__()

        if count != 1:
            return "Jogador não existe"
        elif count == 1:
            query = f"""UPDATE jogador SET                 
                peso = {self.peso},
                altura = {self.altura},
                pos = '{self.pos}',
                classif = {self.classif},
                equipa = {self.equipa}
                WHERE nome = '{self.nome}';"""

            SQL_handler.update_data(query)
            return "Jogador atualizado com sucesso!!!"

class Equipa(BaseModel):
    nome: str
    estadio: str
    cidade: str
    abrev: str
    ano: int

    def AddToDB(self):
        conn = sqlite3.connect('jogadores.db')
        cur = conn.cursor()
        query = f"""INSERT INTO clube (nome, estadio, cidade, abrev, ano) VALUES (
            '{self.nome}',
            '{self.estadio}',
            '{self.cidade}',
            '{self.abrev}',
            {self.ano});"""

        print(query)

        cur.execute(query)
        conn.commit()
        conn.close()

    def UpdateDB(self):
        getData = f"""SELECT * FROM clube WHERE nome = '{self.nome}'"""
        count =  SQL_handler.select_data(getData).__len__()

        if count != 1:
            return "Clube não existe"
        elif count == 1:
            query = f"""UPDATE clube SET
                estadio = '{self.estadio}',
                cidade = '{self.cidade}',
                abrev = '{self.abrev}',
                ano = {self.ano}
                WHERE nome = '{self.nome}';"""

            SQL_handler.update_data(query)
            return "Clube atualizado com sucesso!!!"

