import sqlite3
from pydantic import BaseModel
from SQL_handler import SQL_handler

class Alunos(BaseModel):
    nome: str
    apelido: str
    idade: int
    nota1: float
    nota2: float
    nota3: float
    nota4: float
    media: float
    resultado: str
    performance: str


    def AddToDB(self):
        self.media = self.AddAvarage()
        self.resultado = self.AddResult()
        self.performance = self.AddPerform()

        query = f"""INSERT INTO pauta (nome, apelido, idade, nota1, nota2, nota3, nota4,
        media, resultado, aproveitamento) VALUES (            
            '{self.nome}',
            '{self.apelido}',
            {self.idade},
            {self.nota1},
            {self.nota2},
            {self.nota3},
            {self.nota4},
            {self.media},
            '{self.resultado}',
            '{self.performance}'
            );"""
        SQL_handler.update_data(query)


    def AddAvarage(self):
        media = round((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4, 2)
        return media

    def AddResult(self):
        if self.media >= 10:
            return "aprovado"
        else:
            return "reprovado"

    def AddPerform(self):
        if self.media < 5:
            performance = "mau"
        elif self.media < 10:
            performance = "insuficiente"
        elif self.media < 15:
            performance = "suficiente"
        elif self.media < 18:
            performance = "bom"
        else:
            performance = "muito Bom"
        return performance

    def UpdateDB(self):
        getData = f"""SELECT * FROM pauta WHERE nome = '{self.nome}';"""
        count = SQL_handler.select_data(getData).__len__()

        if count != 1:
            return "Aluno não existe"
        elif count == 1:
            self.media = self.AddAvarage()
            self.resultado = self.AddResult()
            self.performance = self.AddPerform()
            query = f"""UPDATE pauta SET                 
                nome = '{self.nome}',
                apelido = '{self.apelido}',
                idade = {self.idade},
                nota1 = {self.nota1},
                nota2 = {self.nota2},
                nota3 = {self.nota3},
                nota4 = {self.nota4},
                media = {self.media},
                resultado = '{self.resultado}',
                aproveitamento = '{self.performance}'
                WHERE nome = '{self.nome}' AND apelido = '{self.apelido}';"""

            SQL_handler.update_data(query)
            return "Aluno atualizado com sucesso!!!"

