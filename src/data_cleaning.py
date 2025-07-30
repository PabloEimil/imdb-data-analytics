import pandas as pd
import numpy as np

def clean_name_basics(df: pd.DataFrame):
    r""" 
    Limpia el dataset name.basics.
    1. Convierte birthYear y deathYear en numero entero
    2. Elimina posibles espacios en primaryName
    3. Sustituye valores \N por unknown y las transforma en listas ya que tienen varios datos
    4. Elimina posibles duplicados.
    
    Parametros: 
        df: dataframe de name.basics cargado en data_loader
        
    Output: 
        df: Dataframe limpio y procesado
        """
    
    df= df.copy()

    #1
    for c in ["birthYear", "deathYear"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

    #2
    if "primaryName" in df.columns:
        df["primaryName"] = df["primaryName"].str.strip()

    #3
    for c in ["primaryProfession", "knownForTitles"]:
        if c in df.columns:
            df[c] = df[c].replace(r"\N", np.nan).fillna("unknown").str.split(",")

    #4
    if "nconst" in df.columns:
        df = df.drop_duplicates(subset="nconst")

    return df

