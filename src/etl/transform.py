import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import ExtraTreesRegressor

# Transformações nos dados extraídos

def clean_brick(df):
    df_clean = df.copy() 
    df_clean.dropna(how='all',inplace=True)
    df_clean = transform_brick(df_clean)
    df_clean['rua'].fillna('Sem Referência', inplace=True)
    df_clean = df_clean.iloc[:, 2:]
    unique_bricks = set(tuple(row) for row in df_clean.values)
    return unique_bricks

def clean_filial(df):
    df_clean = df.copy()
    df_clean = transform_brick(df_clean)
    df_clean = df_clean.rename(columns={'Cód. Filial':'filial'})
    return df_clean


def transform_sales_price(df):
    ''''Transformação dos dados de sales_price, Perecebi que o EAN, Brick e Cod Prod Catarinense nunca serão nulos, pois são chaves de identificação dos produtos e filials.
    Estou adicionando o tratamento de valores nulos apenas para as colunas numéricas de vendas apartir das colunas númericas existentes no dataframe, para ter uma média de valores mais precisas e coerentes com a realidade do que usar a média simples ou mediana que poderia afetar a visualização dos dados.
    '''
    df_copy = df.copy()
    df_renamed = change_columns_sales(df_copy)
    df_renamed = transform_brick(df_renamed)

    #num_cols = df_renamed.select_dtypes(include='number').columns

    '''
    Usando IterativeImputer com ExtraTreesRegressor para imputar valores nulos. Essa abordagem não seria interessante nesse caso pois tem baixa quantidade de dados para treinar o modelo de regressão.
    Porém deixo o código comentado aqui como referência para futuros projetos com datasets maiores. E um conceito novo que estou aprendendo e gostaria de aplicar em projetos futuros.
    imputer = IterativeImputer(
        estimator=ExtraTreesRegressor(n_estimators=30, random_state=42),
        max_iter=10,
        random_state=42
    )
    df_renamed[num_cols] = imputer.fit_transform(df_renamed[num_cols])
    df_renamed[num_cols] = df_renamed[num_cols].clip(lower=0).round()

    '''
    # Imputação simples usando a médiana para colunas numéricas
    num_cols = df_renamed.select_dtypes(include='number').columns
    for col in num_cols:
        if (df_renamed[col] == 0).any():
            df_renamed[col].replace(0, np.nan, inplace=True)
            df_renamed[col].fillna(df_renamed[col].median(), inplace=True)
        else:
            df_renamed[col].fillna(df_renamed[col].median(), inplace=True)
        df_renamed[col] = df_renamed[col].clip(lower=0).round()
    
    # Removendo linhas que ainda possuem todos os valores nulos (se houver)
    df_renamed.dropna(how='all',inplace=True)
    return df_renamed

def change_columns_sales(df):
    '''
    Essa função renomeia as colunas do DataFrame para nomes mais amigáveis.
    1. brick: Identificador do Brick
    2. ean: Código EAN do produto
    3. cod_prod_catarinense: Código do Produto Catarinense
    4. vendas_concorr_indep_unid: Vendas em unidades para concorrentes independentes
    5. vendas_grandes_concorr_unid: Vendas em unidades para grandes concorrentes
    6. venda_preco_popular_unid: Vendas em unidades para a  preço popular - filial da clamed
    '''
    df = df.set_axis(['brick','ean','cod_prod_catarinense','vendas_concorr_indep_unid','vendas_grandes_concorr_unid',
    'venda_preco_popular_unid'], axis='columns')
    return df

def transform_brick(df):
    df[['id','cidade','rua'] ]= df['brick'].str.split('-', n=2, expand=True)
    return df