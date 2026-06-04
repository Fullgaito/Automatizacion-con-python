import pandas as pd

#leer el archivo excel
df = pd.read_excel('C:/Users/Sergio/Documents/Automatizacion-con-python/PRODUCTOS.xlsx')

#filtrar articulo precio mayor a 300
articulo_mayor_300 = df[df['PRECIO'] >= 300]

#ordenar articulos
articulo_ordenado = articulo_mayor_300.sort_values(by='PRECIO', ascending=True)

#guardar en nuevo excel info filtrada
salida="C:/Users/Sergio/Documents/Automatizacion-con-python"
articulo_ordenado.to_excel(salida + '/articulo_mayor_300.xlsx', index=False)