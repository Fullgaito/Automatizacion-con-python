import pandas as pd
import os

ruta = 'C:/Users/Sergio/Documents/Automatizacion-con-python/PRODUCTOS.xlsx'
df = pd.read_excel(ruta,parse_dates=['FECHA'])

carpeta_salida = 'C:/Users/Sergio/Documents/Automatizacion-con-python/productos_por_año'
os.makedirs(carpeta_salida, exist_ok=True)

#crear una nueva columna solo con el año
df['AÑO'] = df['FECHA'].dt.year

#obtener valores unicos de nueva columna
años_unicos = df['AÑO'].dropna().unique()
for año in años_unicos:
    df_año = df[df['AÑO'] == año]
    nombre_archivo = f'productos_{int(año)}.xlsx'
    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
    df_año.to_excel(ruta_salida, index=False)

