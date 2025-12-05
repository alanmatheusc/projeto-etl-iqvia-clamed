import psycopg2 as pg
import os
from dotenv import load_dotenv

load_dotenv()  

def connect_db():
  try:
    conn = pg.connect(
    host=os.getenv("DATABASE_URL"),
    database=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    port=os.getenv("DATABASE_PORT")
  )
    return conn
  except Exception as e:
    return f"Erro ao conectar ao banco de dados: {e}"
