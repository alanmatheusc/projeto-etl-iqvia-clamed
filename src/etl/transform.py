from src.etl.extract import *

# Transformações nos dados extraídos
def clean_brick(df=filial_brick):
    df_clean = df.copy()

    # Quero apenas valores únicos na coluna 'brick'
    unique_brick = pd.DataFrame(set(df_clean['brick']))
    if(unique_brick.isna().sum() >= 0):
      unique_brick = unique_brick.dropna().reset_index(drop=True)
    unique_brick.str.upper()
    return unique_brick
