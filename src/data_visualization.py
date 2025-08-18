import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from itertools import combinations
import seaborn as sns

def gen_type_popular_bar (df: pd.DataFrame):

    bar1= df.groupby("titleType")["numVotes"].sum().sort_values(ascending=False)
    bar2= df.groupby("titleType")["numVotes"].mean().sort_values(ascending=False)

    df_exploded= df.explode("genres")
    bar3 = df_exploded.groupby("genres")["numVotes"].sum().sort_values(ascending=False).head(12)
    bar4 = df_exploded.groupby("genres")["numVotes"].mean().sort_values(ascending=False).head(12)

    fig, ax = plt.subplots (2,2, figsize=(15,10))

    ax[0,0].bar(bar1.index, bar1.values, color="#F5BE27", edgecolor= "black", linewidth= 1.0)
    ax[0,0].set_title("1. Nº de votos totales por tipo", fontweight= "bold")
    ax[0,0].grid(True, axis= "y", linestyle="--", alpha= 0.4)
    ax[0,0].set_ylabel("Miles de millones de votos", fontsize= 8.5) 
    ax[0,0].set_facecolor("#E8F1FA")

    ax[0,1].bar(bar2.index, bar2.values, color= "#4094E3", edgecolor= "black", linewidth= 1.0)
    ax[0,1].set_title("2. Nº de votos proporcional por tipo", fontweight= "bold")
    ax[0,1].grid(True, axis= "y", linestyle="--", alpha= 0.4)
    ax[0,1].set_facecolor("#E8F1FA")

    ax[1,0].bar(bar3.index, bar3.values, color="#F5BE27", edgecolor= "black", linewidth= 1.0)
    ax[1,0].set_title("3. Nº de votos totales por género", fontweight= "bold")
    ax[1,0].grid(True, axis= "y", linestyle="--", alpha= 0.4)
    ax[1,0].set_ylabel("Cientos de millones de votos", fontsize= 8.5) 
    ax[1,0].tick_params(axis="x", rotation=45)
    ax[1,0].set_facecolor("#E8F1FA")

    ax[1,1].bar(bar4.index, bar4.values, color= "#4094E3", edgecolor= "black", linewidth= 1.0)
    ax[1,1].set_title("4. Nº de votos proporcional por género", fontweight= "bold")
    ax[1,1].grid(True, axis= "y", linestyle="--", alpha= 0.4)
    ax[1,1].tick_params(axis="x", rotation=45)
    ax[1,1].set_facecolor("#E8F1FA")

    plt.tight_layout()
    plt.show()



def gen_type_most_popular_hbar (df: pd.DataFrame):

    df_exploded= df.explode("genres")
    bar1=df_exploded.groupby("genres")["averageRating"].mean().sort_values(ascending=True).tail(6)
    bar2=df_exploded.groupby("genres")["averageRating"].mean().sort_values(ascending=True).head(6)
    bar3= df.groupby("titleType")["averageRating"].mean().sort_values(ascending=True)

    fig, ax = plt.subplots (2,2, figsize=(15,8))

    ax[0,0].barh(bar1.index, bar1.values, color="#4094E3", edgecolor= "black", linewidth= 1.0)
    ax[0,0].set_title("1. TOP 6 con MEJOR nota media por género", fontweight= "bold")
    ax[0,0].grid(True, axis= "x", linestyle="--", alpha= 0.4)
    ax[0,0].set_xlim(5, 7.5)
    ax[0,0].set_facecolor("#E8F1FA")

    ax[0,1].barh(bar2.index, bar2.values, color="#4094E3", edgecolor= "black", linewidth= 1.0)
    ax[0,1].set_title("2. TOP 6 con PEOR nota media por género", fontweight= "bold")
    ax[0,1].grid(True, axis= "x", linestyle="--", alpha= 0.4)
    ax[0,1].set_xlim(5, 7.5)
    ax[0,1].set_facecolor("#E8F1FA")

    ax[1,0].barh(bar3.index, bar3.values, color="#F5BE27", edgecolor= "black", linewidth= 1.0)
    ax[1,0].set_title("3. Nota media por tipo", fontweight= "bold")
    ax[1,0].grid(True, axis= "x", linestyle="--", alpha= 0.4)
    ax[1,0].set_xlim(5, 7.5)
    ax[1,0].set_facecolor("#E8F1FA")

    ax[1,1].axis("off")

    plt.tight_layout()
    plt.show()



def valor_num_relation_scatter(df: pd.DataFrame):

    scatter1 = df[df["numVotes"] >= 50]  

    plt.figure(figsize=(10, 6))
    plt.scatter(scatter1["numVotes"], scatter1["averageRating"], alpha=0.1, s=10)

    x = np.log10(scatter1["numVotes"])
    y = scatter1["averageRating"]
    m, b = np.polyfit(x, y, 1)
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = m * x_fit + b
    plt.plot(10**x_fit, y_fit, color="#F5BE27", linewidth=3, label="Tendencia")

    plt.xscale("log")
    plt.xlabel("Número de votos (log)")
    plt.ylabel("Valoración")
    plt.title("Relación entre nº de votos y valoración", fontweight="bold")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.3)
    plt.show()



def valor_num_gen_relation_plot (df: pd.DataFrame):

    df_exploded = df.explode("genres")

    df_genres = df_exploded.groupby("genres").agg({
        "numVotes": "sum",
        "averageRating": "mean"
    }).sort_values("numVotes", ascending=False).reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(df_genres["genres"], df_genres["numVotes"], color="#4094E3", label="Número de votos", marker="o")
    ax1.set_xlabel("Género",  alpha=0.8)
    ax1.set_ylabel("Número de votos", alpha=0.8)
    ax1.set_xticks(range(len(df_genres["genres"])))
    ax1.set_xticklabels(df_genres["genres"], rotation=45, ha="right")
    ax1.set_yscale("log")

    ax2 = ax1.twinx()
    ax2.plot(df_genres["genres"], df_genres["averageRating"], color="#F5BE27", label="Nota media", marker="s")
    ax2.set_ylabel("Nota media", alpha=0.8)
    ax2.set_ylim(4, 9)

    linea_votos, = ax1.plot(df_genres["genres"], df_genres["numVotes"], color="#4094E3", label="Número de votos", marker="o")
    linea_nota, = ax2.plot(df_genres["genres"], df_genres["averageRating"], color="#F5BE27", label="Valoración media", marker="s")

    lines = [linea_votos, linea_nota]
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc="upper right")

    plt.title("Relación entre número de votos y valoración media por género", fontweight="bold")
    fig.tight_layout()
    ax1.grid(axis="x", linestyle="--", alpha=0.2)
    ax1.set_facecolor("#E8F1FA")
    plt.show()



def mov_year_plot (df: pd.DataFrame):

    df= df.groupby("startYear").size().reset_index(name="count")
    df = df[df["startYear"] != 2025]

    plt.figure(figsize=(12,6))
    plt.plot(df["startYear"], df["count"], linewidth=3, color="#4094E3")
    plt.title("Número de películas por año", fontweight="bold")
    plt.xlabel("Año de estreno")
    plt.ylabel("Cantidad de películas")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()



def rat_year_plot (df: pd.DataFrame):

    df= df.groupby("startYear")["averageRating"].mean().reset_index()
    df= df[df["startYear"].between(1912, 2024)]
    df["rolling_mean"] = df["averageRating"].rolling(window=5).mean()

    plt.figure(figsize=(12,6))
    plt.plot(df["startYear"], df["rolling_mean"], linewidth=3, color="#4094E3")
    plt.title("Evolución de la valoración por año", fontweight="bold")
    plt.xlabel("Año de estreno")
    plt.ylabel("Valoración promedio (1-10)")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()



def gen_year_plot (df: pd.DataFrame):

    df= df.explode("genres")
    df= df.groupby(["startYear", "genres"]).size().reset_index(name="num_titles")
    df=df[df["startYear"].between(1950,2024)]
    top_df= df.groupby("genres")["num_titles"].sum().sort_values(ascending=False).head(8).index

    pivot = df.pivot(index="startYear", columns="genres", values="num_titles").fillna(0)
    pivot_top = pivot[top_df]
    pivot_top_smooth = pivot_top.rolling(window=2, min_periods=1).mean()
    pivot_top_smooth.plot.area(figsize=(14,8), alpha=0.6)

    plt.title("Popularidad del TOP 8 géneros a lo largo del tiempo", fontweight="bold")
    plt.ylabel("Número de títulos lanzados")
    plt.xlabel("Año")
    plt.grid(True, axis= "x", linestyle="--", alpha=0.3)
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()



def dur_year_plot (df: pd.DataFrame):

    df= (df.groupby("startYear")["runtimeMinutes"].mean().reset_index().sort_values("startYear"))
    df= df[df["startYear"].between(1950, 2024)]

    plt.figure(figsize=(10,6))
    plt.fill_between(df["startYear"], df["runtimeMinutes"], color="skyblue", alpha=0.4)
    plt.plot(df["startYear"], df["runtimeMinutes"], color="#4094E3")
    plt.xlabel("Año de estreno")
    plt.ylabel("Duración promedio")
    plt.title("Evolución de la duración promedio de películas por año", fontweight="bold")
    plt.ylim(60, df["runtimeMinutes"].max() * 1.10)
    plt.gca().set_facecolor("#E8F1FA")
    plt.grid(True, alpha= 0.3)
    plt.show()


def gen_study_bar (df: pd.DataFrame):

    df = df.explode("genres")
    df = df.groupby("genres").agg(
        num_titles=("averageRating", "count"),
        mean_votes=("numVotes", "mean"),
        avg_rating=("averageRating", "mean")
    ).reset_index().sort_values("num_titles", ascending=False)

    cmap = plt.cm.Reds
    colors = cmap(df["mean_votes"] / df["mean_votes"].max())

    fig, ax1 = plt.subplots(figsize=(17, 7))

    bars = ax1.bar(
        df["genres"],
        df["num_titles"],
        color=colors, zorder=3
    )
    ax1.set_ylabel("Número de películas")
    ax1.set_xticks(range(len(df["genres"])))
    ax1.set_xticklabels(df["genres"], rotation=70)
    ax1.set_title("Nº de películas, valoración y numero de votos por género", fontweight= "bold")

    ax2 = ax1.twinx()
    ax2.plot(df["genres"], df["avg_rating"], color="#4094E3", marker="o", linewidth=3, label="Valoración media")
    ax2.set_ylabel("Valoración media")
    ax2.set_ylim(0, 10)

    sm = plt.cm.ScalarMappable(cmap=cmap, 
                            norm=plt.Normalize(vmin=df["mean_votes"].min(), 
                                                vmax=df["mean_votes"].max()))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=[ax1, ax2])
    cbar.set_label("Promedio nº de votos")

    ax2.legend(loc="upper right")
    ax1.set_facecolor("#E8F1FA")
    ax1.grid(True, axis= "x", linestyle="--", alpha= 0.2, zorder=0)
    fig.subplots_adjust(right=0.74)
    plt.show()  



def var_rel_pivot (df: pd.DataFrame):

    df = df.loc[:, ~df.columns.duplicated()].reset_index(drop=True)
    df_filtrado = df[df["runtimeMinutes"] <= 240].copy()

    dur_bins = np.arange(0, 260, 20)
    df_filtrado["duracion_bin"] = pd.cut(df_filtrado["runtimeMinutes"], bins=dur_bins)

    rating_bins = np.arange(0, 11, 1)
    df_filtrado["rating_bin"] = pd.cut(df_filtrado["averageRating"], bins=rating_bins)

    heat_data = df_filtrado.pivot_table(
        index="duracion_bin",
        columns="rating_bin",
        values="numVotes",
        aggfunc="mean",
        fill_value=0,
        observed=False
    )

    plt.figure(figsize=(12, 7))
    sns.heatmap(heat_data, cmap="Blues", annot=True, fmt=".0f", cbar_kws={"label": "Número promedio de votos"})
    plt.title("Distribución de películas por duración y valoración", fontweight="bold")
    plt.xticks(fontsize=10, fontweight="bold", rotation=45)
    plt.yticks(fontsize=10, fontweight="bold")
    plt.xlabel("Valoración promedio")
    plt.ylabel("Duración")
    plt.show()



def val_dur_bar (df: pd.DataFrame):

    df_filtrado = df[df["runtimeMinutes"] <= 240].copy()
    dur_bins = np.arange(0, 260, 20)
    df_filtrado["duracion_bin"] = pd.cut(df_filtrado["runtimeMinutes"], bins=dur_bins)

    rating_por_duracion = df_filtrado.groupby("duracion_bin", observed=False)["averageRating"].mean().reset_index()
    rating_por_duracion["duracion_bin"] = rating_por_duracion["duracion_bin"].astype(str)

    # Graficar
    plt.figure(figsize=(14, 6))
    plt.bar(rating_por_duracion["duracion_bin"], rating_por_duracion["averageRating"], color="#4094E3", edgecolor= "black")

    plt.title("Valoración promedio por rango de duración", fontsize=16, fontweight="bold")
    plt.xlabel("Duración (mins)", fontsize=9)
    plt.ylabel("Valoración promedio", fontsize=9)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(True, axis= "y", linestyle="--", alpha=0.3)
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()



def gen_dur_bar (df: pd.DataFrame):

    df= df.explode("genres")

    genre_runtime = (
        df.groupby("genres")["runtimeMinutes"]
        .mean()
        .reset_index()
        .sort_values("runtimeMinutes", ascending=False)
    )

    plt.figure(figsize=(10,10))
    plt.barh(genre_runtime["genres"], genre_runtime["runtimeMinutes"], color="#4094E3", edgecolor= "black")
    plt.xlabel("Media de duración (min)")
    plt.ylabel("Género")
    plt.title("Duración promedio por género", fontweight="bold")
    plt.gca().invert_yaxis()
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()



def top_genre_pairs(df, genre_filter=None):
    
    if genre_filter is not None:
        df = df[df["genres"].apply(
            lambda g: isinstance(g, list) and any(str(gen).strip().lower() == genre_filter.lower() for gen in g))
        ].copy()
    else:
        df = df.copy()
    
    def get_pairs(genres):
        if isinstance(genres, list) and len(genres) >= 2:
            return [tuple(sorted(pair)) for pair in combinations(genres, 2)]
        return []
    
    df["genre_pairs"] = df["genres"].apply(get_pairs)
    
    df_pairs = df.explode("genre_pairs").dropna(subset=["genre_pairs"])
    if genre_filter is not None:
        df_pairs = df_pairs[df_pairs["genre_pairs"].apply(lambda pair: genre_filter in pair)]

    genre_weights = {
        "Adult":0.3, "Talk-Show":0.3, "Reality-TV":0.3, "Game-Show":0.3,
        "News":0.5, "Film-Noir":0.5, "Sport":0.5, "Western":0.5, "Short":0.5,
        "Horror":0.7, "Sci-Fi":0.7, "Misterio":0.7, "Musical":0.7, "Animación":0.7,
        "Guerra":0.8, "Familia":0.8, "Fantasía":0.8, "Música":0.8, "Biografía":0.8,
        "Documental":0.9, "Accion":0.9, "Romance":0.9, "Historia":0.9, "Comedia":0.9,
        "Drama":1.0, "Aventura":1.0, "Crimen":1.0, "Thriller":1.0}
    
    df_pairs["weight"] = df_pairs["genre_pairs"].apply(lambda pair: (genre_weights.get(pair[0],0.5)+genre_weights.get(pair[1],0.5))/2)
    
    df_pairs["votes_log"] = np.log1p(df_pairs["numVotes"])
    df_pairs["total_votes_log"] = np.log1p(df_pairs.groupby("genre_pairs")["numVotes"].transform("sum"))
    
    df_pairs["rating_norm"] = (df_pairs["averageRating"] - df_pairs["averageRating"].min()) / \
                              (df_pairs["averageRating"].max() - df_pairs["averageRating"].min())
    df_pairs["votes_norm"] = (df_pairs["votes_log"] - df_pairs["votes_log"].min()) / \
                             (df_pairs["votes_log"].max() - df_pairs["votes_log"].min())    
    df_pairs["total_votes_norm"] = (df_pairs["total_votes_log"] - df_pairs["total_votes_log"].min()) / \
                                   (df_pairs["total_votes_log"].max() - df_pairs["total_votes_log"].min())    
    df_pairs["total_score"] = (0.4 * df_pairs["rating_norm"] +
                               0.5 * df_pairs["votes_norm"] +
                               0.1 * df_pairs["total_votes_norm"]) * df_pairs["weight"]

    pairs_stats = df_pairs.groupby("genre_pairs").agg(
        avg_rating=("averageRating","mean"),
        total_votes=("numVotes","sum"),
        avg_votes=("numVotes","mean"),
        avg_score=("total_score","mean"),
        count_titles=("tconst","count")
    ).reset_index()
    
    pairs_stats = pairs_stats[pairs_stats["avg_votes"] >= 500]
    
    top_pairs = pairs_stats.sort_values("avg_score", ascending=False).head(10)
    
    if genre_filter:
        print(f"Top 10 combinaciones de géneros que incluyen '{genre_filter}':\n")
    else:
        print("Top 10 combinaciones de géneros:\n")

    for i, row in top_pairs.iterrows():
        print(f"{row['genre_pairs']} → Puntuación: {row['avg_score']:.2f} | "
            f"Rating Promedio: {row['avg_rating']:.2f} | "
            f"Votos Promedio: {row['avg_votes']:.0f} | "
            f"Votos totales: {row['total_votes']}")



def top_gen_df (df: pd.DataFrame, df1: pd.DataFrame):

    df_top= df.explode("genres")
    conteo_top= df_top["genres"].value_counts(normalize=True)*100

    df_all= df1.explode("genres")
    conteo_all= df_all["genres"].value_counts(normalize=True)*100

    comparacion = pd.DataFrame({
        "% Top1": conteo_top,
        "% Total": conteo_all
        
    }).fillna(0)

    comparacion["Diferencia"] = comparacion["% Top1"] - comparacion["% Total"]
    comparacion = comparacion.sort_values("% Top1", ascending=False)
    for col in comparacion.columns:
        comparacion[col] = comparacion[col].map(lambda x: f"{x:.1f}%")

    return comparacion.head(10)



def top_dur_df (df: pd.DataFrame, df1: pd.DataFrame):

    df_dur = df[(df["runtimeMinutes"] >= 60) & (df["runtimeMinutes"] <= 200)]
    df_dur= df_dur.groupby("runtimeMinutes")["tconst"].count().reset_index(name="num_titles")
    df_dur["perc"] = 100 * df_dur["num_titles"] / df_dur["num_titles"].sum()

    all_dur = df1[(df1["runtimeMinutes"] >= 60) & (df1["runtimeMinutes"] <= 200)]
    all_dur= all_dur.groupby("runtimeMinutes")["tconst"].count().reset_index(name="num_titles")
    all_dur["perc"] = 100 * all_dur["num_titles"] / all_dur["num_titles"].sum()

    plt.figure(figsize=(10,6))
    plt.plot(all_dur["runtimeMinutes"], all_dur["perc"], 
            label="Todas las películas", alpha=0.7, color="#4094E3", linewidth=2)
    plt.plot(df_dur["runtimeMinutes"], df_dur["perc"], 
            label="Top 1%", alpha=0.9, color="#F5BE27", linewidth=2)

    plt.xlabel("Duración (minutos)")
    plt.ylabel("Porcentaje de títulos (%)")
    plt.title("Distribución relativa de títulos por duración", fontweight="bold")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.gca().set_facecolor("#E8F1FA")
    plt.show()

    
# AQUI IRAN FORMULAS PARA LA VISUALIZACIÓN

