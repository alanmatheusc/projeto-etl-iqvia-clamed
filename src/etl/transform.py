import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import ExtraTreesRegressor


# Transformações nos dados extraídos
def clean_brick(df):
    df_clean = df.copy()  
    # Quero apenas valores únicos na coluna 'brick'
    unique_brick = pd.DataFrame(set(df_clean['brick']))
    unique_brick.dropna(inplace=True)
    return unique_brick

def clean_filial(df):
    df_clean = df.copy()  
    df_clean.columns = ['brick', 'filial']
    return df_clean

def transform_sales_price(df):
    ''''Transformação dos dados de sales_price, Perecebi que o EAN, Brick e Cod Prod Catarinense nunca serão nulos, pois são chaves de identificação dos produtos e filials.
    Estou adicionando o tratamento de valores nulos apenas para as colunas numéricas de vendas apartir das colunas númericas existentes no dataframe, para ter uma média de valores mais precisas e coerentes com a realidade do que usar a média simples ou mediana que poderia afetar a visualização dos dados.
    '''
    df_copy = df.copy()
    df_renamed = change_column_names(df_copy)
    num_cols = df_renamed.select_dtypes(include='number').columns

    # Usando IterativeImputer com ExtraTreesRegressor para imputar valores nulos.
    imputer = IterativeImputer(
        estimator=ExtraTreesRegressor(n_estimators=30, random_state=42),
        max_iter=10,
        random_state=42
    )
    df_renamed[num_cols] = imputer.fit_transform(df_renamed[num_cols])
    df_renamed[num_cols] = df_renamed[num_cols].clip(lower=0).round()

    # Removendo linhas que ainda possuem todos os valores nulos (se houver)
    df_renamed.dropna(how='all',inplace=True)
    return df_renamed

def change_column_names(df):
    df = df.set_axis(['brick','ean','cod_prod_catarinense','vendas_concorr_indep_unid','vendas_grandes_concorr_unid',
    'venda_preco_popular_unid'], axis='columns')
    return df