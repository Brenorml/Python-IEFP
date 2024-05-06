import sqlite3
from SQL_handler import SQL_handler

table = """SELECT jogador.*, clube.abrev FROM jogador JOIN
        clube ON jogador.equipa = clube.id;"""
lista = SQL_handler.select_data(table)
print(lista)

