from src.etl import transform as t, extract as e, load as l
from src.database import queries as query

def pipeline_brick():
    filial_brick = e.filial_brick

    set_brick = t.clean_brick(filial_brick)

    l.insert_into_brick_table(set_brick)