import pandas as pd

def resumen_df(df: pd.DataFrame) -> pd.DataFrame:
    r"""
    Muestra informacion básica del df 
    """
    n_filas, n_columnas = df.shape
    duplicadas = df.duplicated().sum()
    nulos_totales = df.isnull().sum().sum()

    print(f"🔵Resumen del dataset:")
    print(f"  🔸Filas: {n_filas}")
    print(f"  🔸Columnas: {n_columnas}")
    print(f"  🔸Filas duplicadas: {duplicadas}")
    print(f"  🔸Datos nulos totales: {nulos_totales}")
    print("\n🔵Columnas y tipos de datos:")
    print(df.dtypes)
    nulos_columna = df.isnull().sum()
    nulos_columna = nulos_columna[nulos_columna > 0]
    if not nulos_columna.empty:
        print("\n🔵Nulos por columna (%):")
        print((nulos_columna / len(df) * 100).round(2).astype(str) + "%")
    print("\n🔵Valores únicos por columna:")
    print(df.nunique())
    display(df.head())


