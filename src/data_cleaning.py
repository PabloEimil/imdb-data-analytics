import pandas as pd
import numpy as np


def clean_name_basics(df: pd.DataFrame) -> pd.DataFrame:
    r""" 
    Limpia el dataset name.basics:
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
            df[col] = df[col].replace(r"\N", pd.NA).fillna("unknown").str.split(",")

    #4
    if "nconst" in df.columns:
        df = df.drop_duplicates(subset="nconst")

    return df



def clean_title_akas (df: pd.DataFrame) -> pd.DataFrame:

    r""" 
    Limpia el dataset title.akas:
    1. Elimina columnas inecesarias
    2. Elimina posibles espacios
    3. Agrupa los titulos y las regiones en listas
    4. Cambiamos nombres de columnas
    
    Parametros: 
        df: dataframe de title.akas cargado en data_loader
        
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
            df[col]= df[col].str.strip()

    #3
    df = df.replace(r"\\N", pd.NA)

    grouped = df.groupby("titleId").agg({
        "title": lambda x: [v for v in x.dropna().unique()],
        "region": lambda x: [v for v in x.dropna().unique()]
    }).reset_index()

    #4
    grouped["title"] = grouped["title"].apply(sorted)
    grouped["region"] = grouped["region"].apply(sorted)

    return grouped.rename(columns={"title": "titlesList", "region": "regionList"})


def clean_title_basics (df: pd.DataFrame) -> pd.DataFrame:

    r"""
    Limpia el datase title_basics:
    1. Quitamos posibles espacios en columnas de texto
    2. Convierte columnas numericas a numeros y a nulos registros sin sentido
    3. Convertimos a nulos registros con r"\N"
    4. Convertimos a booleano la columna isAdult
    5. Convertimos genres a lista

    Parametros: 
        df: dataframe de title.basics cargado en data_loader
        
    Output: 
        df: Dataframe limpio y procesado.
    """

    df= df.copy()

    df = df.drop_duplicates(subset="tconst")

    #1
    for col in ["titleType", "primaryTitle", "originalTitle"]:
        if col in df.columns:
            df[col]=df[col].str.strip()
    
    #2
    for col in ["startYear", "endYear", "runtimeMinutes"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    for col in ["startYear", "endYear"]:
        if col in df.columns:
            df.loc[(df[col] < 1850) | (df[col] > 2050), col] = pd.NA

    #3
    for col in ["primaryTitle", "originalTitle", "titleType","genres"]:
        if col in df.columns:
            df[col] = df[col].replace(r"\N", pd.NA)
    
    #4
    if "isAdult" in df.columns:
        df["isAdult"] = df["isAdult"].replace(r"\N", 0).astype(int).astype(bool)
    
    #5
    if "genres" in  df.columns:
        df["genres"]= df["genres"].str.split(",")

    df= df[df["titleType"] != "tvEpisode"]
      
    return df


def clean_title_principals (df: pd.DataFrame) -> pd.DataFrame:

    r"""
    Limpia el dataframe de title.principals.
    1. Elimina la columna ordering
    2. Crea los nulos y elimina posibles espacios
    3. Si el job es igual a category se queda como nulo

    Parametros: 
        df: dataframe de title.basics cargado en data_loader
        
    Output: 
        df: Dataframe limpio y procesado.
    """

    df= df.copy()

    #1
    if "ordering" in df.columns:
        df= df.drop(columns= "ordering")

    #2
    for col in ["category","job", "characters"]:
        if col in df.columns:
            df[col]= df[col].replace(r"\N", pd.NA).str.strip()   

    #3
    if "job" in df.columns and "category" in df.columns:
        df.loc[df["job"] == df["category"], "job"] = pd.NA
       
    return df