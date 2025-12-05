from src.database import queries as query
import pandas as pd

# Carregar dados de um arquivo CSV
filial_brick = pd.read_excel('data/raw/filial-brick_sample.xlsx')

# Inserir dados na tabela dim_brick
df_brick = set(filial_brick['brick'])
query.insert_data_on_brick(df_brick)