from src.etl import transform as t, extract as e, load as l

def pipeline_add_brick_to_dm_brick():
    filial_brick = e.extract_filial_brick()
    set_brick = t.clean_brick(filial_brick)
    l.insert_into_brick_table(set_brick)

def pipeline_add_filial():
    filial_brick = e.extract_filial_brick()
    clean_filial = t.clean_filial(filial_brick)
    print(clean_filial)
    l.insert_into_filial_table(clean_filial)

def pipeline_sales_price():
    sales_price = e.extract_sales_price()
    transformed_sales_price = t.transform_sales_price(sales_price)
    l.insert_into_sales_price_table(transformed_sales_price)

pipeline_add_filial()