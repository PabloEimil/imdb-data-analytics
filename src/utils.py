import pandas as pd
import numpy as np
from src.data_loader import load_imdb_data


def create_episode_df (df: pd.DataFrame):
   

    episodes_df =df[df["titleType"]=="tvEpisode"].copy()

    title_episode_df = load_imdb_data("title.episode.tsv")

    merged_df = episodes_df.merge(
        title_episode_df,
        on="tconst",
        how="left"
    )

    final_df = merged_df[[
        "tconst", "parentTconst", "seasonNumber", "episodeNumber",
        "primaryTitle", "startYear", "runtimeMinutes"
    ]]

    for col in ["seasonNumber", "episodeNumber"]:
        if col in final_df.columns:
            final_df[col] = pd.to_numeric(final_df[col], errors="coerce").astype("Int64")

    return final_df




# AQUI IRÁN OTRAS FORMULAS QUE PUEDEN SER UTILES