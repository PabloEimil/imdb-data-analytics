import pandas as pd
import numpy as np
from src.data_loader import load_imdb_data


def create_episode_df (df: pd.DataFrame) -> pd.DataFrame:
   
    r"""Con las filas de tvEpisode del data frame de title.basics las une a el df de title.episode
    1. Filtramos solo los tvEpisode
    2. Unimos los tvEpisode con el df de title.episode
    3. Filtramos solo las columnas que queremos usar
    4. Convertimos a numérico las filas numéricas
    """
    #1
    episodes_df =df[df["titleType"]=="tvEpisode"].copy()

    #2
    title_episode_df = load_imdb_data("title.episode.tsv")
    merged_df = episodes_df.merge(
        title_episode_df,
        on="tconst",
        how="left"
    )

    #3
    final_df = merged_df[[
        "tconst", "parentTconst", "seasonNumber", "episodeNumber",
        "primaryTitle", "startYear", "runtimeMinutes"
    ]]

    #4
    for col in ["seasonNumber", "episodeNumber"]:
        if col in final_df.columns:
            final_df[col] = pd.to_numeric(final_df[col], errors="coerce").astype("Int64")

    return final_df

def remove_episodes (df: pd.DataFrame) -> pd.DataFrame:

    r""" Elimina del df title.basics todas las filas con tvEpisode de titleType"""

    return df[df["titleType"] != "tvEpisode"].copy()


#PARA RECARGAR LAS SRC, CAMBIAR LOS SRC. (LO QUE SEA)
import importlib
import src.data_analysis
importlib.reload(src.data_analysis)