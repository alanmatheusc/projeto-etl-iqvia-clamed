from src.database import connection
import pandas as pd

def insert_data_on_brick(set):
    connect = connection.connect_db()
    try:
      with connect as conn:
        with conn.cursor() as cursor:
           for value in set:
              print(value)
              cursor.execute("""
              INSERT INTO dim_brick (id_brick,cidade, rua)
              VALUES (%s, %s, %s)
              """, (value[0],value[1],value[2]))
              
        print('inserido com sucesso!')
        conn.commit()
    except Exception as e:
        return f"Erro ao inserir dados: {e}"
    
def insert_data_on_filial(filial):
    connect = connection.connect_db()
    try:
      with connect as conn:
        with conn.cursor() as cursor:
           for index, row in filial.iterrows():
               cursor.execute("""
            INSERT INTO fact_filial (id_filial, fk_brick)
            SELECT %s, id_brick
            FROM dim_brick
            WHERE id_brick = %s
            """, (row['filial'], row['id']))
        conn.commit()
    except Exception as e:
        return f"Erro ao inserir dados: {e}"
    
def insert_data_on_sales_price(sales_price):
    connect = connection.connect_db()
    try:
      with connect as conn:
        with conn.cursor() as cursor:
           for index, row in sales_price.iterrows():
              print(row)
              cursor.execute("""
              INSERT INTO fact_vendas (fk_brick,ean, cod_prod_catarinense, venda_concorr_indep_unid, venda_grandes_concorr_unid, venda_preco_popular_unid)
              SELECT b.id_brick, %s, %s, %s, %s, %s
              FROM dim_brick b
              WHERE b.id_brick = %s
              """, (row['ean'], row['cod_prod_catarinense'], row['vendas_concorr_indep_unid'], row['vendas_grandes_concorr_unid'], row['venda_preco_popular_unid'], row['id']))
              print("Inseridos")
        conn.commit()
    except Exception as e:
        return f"Erro ao inserir dados: {e}"
    

def get_data_from_dim_brick():
    connect = connection.connect_db()
    try:
      with connect as conn:
        query = "SELECT * FROM dim_brick"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return f"Erro ao buscar dados: {e}"
    
def get_data_from_fact_filial():
    connect = connection.connect_db()
    try:
      with connect as conn:
        query = "SELECT * FROM fact_filial"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return f"Erro ao buscar dados: {e}"

def get_data_from_fact_vendas():
    connect = connection.connect_db()
    try:
      with connect as conn:
        query = "SELECT * FROM fact_vendas"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return f"Erro ao buscar dados: {e}"