"""Este programa ordena los archivos en una carpeta específica en subcarpetas según su tipo de archivo.
Las subcarpetas se crean automáticamente si no existen."""

import os 
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def esperar_archivo_libre(ruta_archivo,intentos=10,espera=0.5):
    for _ in range(intentos):
        try:
            with open(ruta_archivo,"rb"):
                return True
        except (IOError, OSError,PermissionError):
            time.sleep(espera)
    return False

def ordenar_archivos():
    #Ruta de la carpeta a ordenar
    ruta="C:/Users/Sergio/Documents"

    #crear carpetas si no existen
    carpetas=["Documentos","Imagenes","PDFS","Hojas de calculo","Documentos de texto","Otros"]
    for carpeta in carpetas:
        if not os.path.exists(os.path.join(ruta,carpeta)):
            os.makedirs(os.path.join(ruta,carpeta))

    #Recorrer los archivos en la carpeta
    for archivo in os.listdir(ruta):
        ruta_archivo=os.path.join(ruta,archivo)
        if os.path.isfile(ruta_archivo):
            if not esperar_archivo_libre(ruta_archivo):
                continue
            extension=os.path.splitext(archivo)[1].lower()
            if extension in [".doc",".docx"]:
                shutil.move(ruta_archivo,os.path.join(ruta,"Documentos",archivo))
            elif extension in [".jpg",".jpeg",".png",".gif"]:
                shutil.move(ruta_archivo,os.path.join(ruta,"Imagenes",archivo))
            elif extension in [".pdf"]:
                shutil.move(ruta_archivo,os.path.join(ruta,"PDFS",archivo))
            elif extension in [".xls",".xlsx"]:
                shutil.move(ruta_archivo,os.path.join(ruta,"Hojas de calculo",archivo))
            elif extension in [".txt"]:
                shutil.move(ruta_archivo,os.path.join(ruta,"Documentos de texto",archivo))
            else:
                shutil.move(ruta_archivo,os.path.join(ruta,"Otros",archivo))

class MiManejador(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            ordenar_archivos()

ordenar_archivos()

manejador=MiManejador()
observador=Observer()
observador.schedule(manejador, path="C:/Users/Sergio/Documents", recursive=False)
observador.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observador.stop()
observador.join()