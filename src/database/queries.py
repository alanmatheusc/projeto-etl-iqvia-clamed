from src.database import connection
import pandas as pd

def insert_data_on_brick(set):
    connect = connection.connect_db()
    try:
      with connect as conn:
        with conn.cursor() as cursor:
           for data in set:
                cursor.execute("INSERT INTO dim_brick (brick) VALUES (%s)", (data,))
        conn.commit()
    except Exception as e:
        return f"Erro ao inserir dados: {e}"