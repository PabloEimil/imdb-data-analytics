import os
import pandas as pd

def get_project_root():
    """Devuelve la ruta del proyecto"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_imdb_data(filename: str, sep="\t"):
    """Devuelve el archivo en una variable de pandas"""
    file_path = os.path.join(get_project_root(), "data", filename)
    df = pd.read_csv(file_path, sep=sep)
    return df

def load_imdb_data_csv(filename: str):
    """Devuelve el archivo en una variable de pandas"""
    file_path = os.path.join(get_project_root(), "data", filename)
    df = pd.read_csv(file_path)
    return df