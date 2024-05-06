import sqlite3

class SQL_handler:
    def select_data(my_query:str):
        conn = sqlite3.connect('estudantes.db')
        cur = conn.cursor()
        print(my_query)
        lista = cur.execute(my_query)
        data = lista.fetchall()
        conn.close()
        return data

    def update_data(my_query: str):
        conn = sqlite3.connect('estudantes.db')
        cur = conn.cursor()
        cur.execute(my_query)
        conn.commit()
        conn.close()
        return True