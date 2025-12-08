from src.database import queries as query
import pandas as pd

def insert_into_brick_table(brick):
    try:
        query.insert_data_on_brick(brick)
    except Exception as e:
        print(f"Erro ao inserir dados na tabela brick: {e}")

def insert_into_filial_table(filial):
    try:
      query.insert_data_on_filial(filial)
    except Exception as e:
        print(f"Erro ao inserir dados na tabela filial: {e}")

def insert_into_sales_price_table(sales_price):
    try:
        query.insert_data_on_sales_price(sales_price)
    except Exception as e:
        print(f"Erro ao inserir dados na tabela sales_price: {e}")

