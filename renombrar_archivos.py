import os

carpeta="C:/Users/Sergio/Downloads"


prefijo="Imagen_"

extension=(".jpg",".jpeg",".png",".gif")

archivos=[]

for nombre_archivo in os.listdir(carpeta):
    if nombre_archivo.lower().endswith(extension):
        archivos.append(nombre_archivo)

for i, nombre_archivo in enumerate(sorted(archivos), start=1):
    _, ext = os.path.splitext(nombre_archivo)
    nuevo_nombre = f"{prefijo}{i:03d}{ext}"
    ruta_antigua = os.path.join(carpeta, nombre_archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)

    if os.path.exists(ruta_nueva):
        contador = 1
        while True:
            nuevo_nombre = f"{prefijo}{i:03d}_{contador}{ext}"
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)
            if not os.path.exists(ruta_nueva):
                break
            contador += 1

    os.rename(ruta_antigua, ruta_nueva)