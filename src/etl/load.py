from src.database import queries as query
import pandas as pd

def insert_into_brick_table(brick):
    try:
        query.insert_data_on_brick(brick)
    except Exception as e:
        print(f"Erro ao inserir dados na tabela brick: {e}")