import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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

    
# AQUI IRAN FORMULAS PARA LA VISUALIZACIÓN

