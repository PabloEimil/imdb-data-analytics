import pandas as pd
import numpy as np


def clean_name_basics(df: pd.DataFrame) -> pd.DataFrame:
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
    for col in ["birthYear", "deathYear"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    #2
    if "primaryName" in df.columns:
        df["primaryName"] = df["primaryName"].str.strip()

    #3
    for col in ["primaryProfession", "knownForTitles"]:
        if col in df.columns:
            df[col] = df[col].replace(r"\N", np.nan).fillna("unknown").str.split(",")

    #4
    if "nconst" in df.columns:
        df = df.drop_duplicates(subset="nconst")

    return df



def clean_title_akas (df: pd.DataFrame) -> pd.DataFrame:

    r""" Limpia el dataset title.akas.
    1. Elimina columnas inecesarias
    2. Elimina posibles espacios
    3. Agrupa los titulos y las regiones en listas
    
    Parametros: 
        df: dataframe de name.basics cargado en data_loader
        
    Output: 
        df: Dataframe limpio y procesado.
    """

    df= df.copy()

    #1
    for col in ["ordering", "types", "attributes", "language", "isOriginalTitle"]:
        if col in df.columns:
            df= df.drop(columns=[col])
    
    #2
    for col in ["title", "region"]:
        if col in df.columns:
            df[col].str.strip()

    #3
    df= df.groupby("titleId").agg({
        "title": lambda x: sorted(set(t for t in x if t!= "\\N" and pd.notna(t))), 
        "region":lambda x: sorted(set(t for t in x if t!= "\\N" and pd.notna(t)))
        }).reset_index()

    #4
    df= df.rename(columns= {"title": "titlesList", "region":"regionList"})

    return df


def clean_title_basics (df: pd.DataFrame) -> pd.DataFrame:



    return df
