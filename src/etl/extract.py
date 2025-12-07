import pandas as pd

def extract_filial_brick():
    filial_brick = pd.read_excel('data/raw/filial-brick_sample.xlsx')
    return filial_brick

def extract_sales_price():
    sales_price = pd.read_excel('data/raw/MS_12_2022_sample.xlsx',dtype={'EAN':'string','Cod Prod Catarinense':'string'})
    return sales_price