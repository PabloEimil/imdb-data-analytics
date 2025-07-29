import pandas as pd

def load_imdb_data (filepath: str):
    """Convierte el dataset en un dataframe para su uso en pandas"""
    df= pd.read_csv(filepath, sep='\t')
    return df