import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

from docx2pdf import convert

SUPPORTED_EXTENSIONS = {".docx", ".doc"}


def obtener_archivos_compatibles(carpeta: Path) -> list[Path]:
    archivos = []
    for ruta in carpeta.rglob("*"):
        if ruta.is_file() and ruta.suffix.lower() in SUPPORTED_EXTENSIONS:
            archivos.append(ruta)
    return sorted(archivos)


def convertir_archivo(ruta_archivo: Path, ruta_salida: Path) -> None:
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    convert(str(ruta_archivo), str(ruta_salida))


def main() -> None:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    pregunta = messagebox.askquestion(
        title="Modo de conversión",
        message="¿Deseas seleccionar archivos individuales?"
    )

    if pregunta == "yes":
        rutas = filedialog.askopenfilenames(
            title="Selecciona archivos .docx/.doc",
            filetypes=[("Documentos Word", "*.docx *.doc")]
        )
        archivos_a_convertir = [Path(ruta) for ruta in rutas]
    else:
        carpeta_entrada = filedialog.askdirectory(title="Selecciona la carpeta de entrada")
        if not carpeta_entrada:
            return
        archivos_a_convertir = obtener_archivos_compatibles(Path(carpeta_entrada))

    if not archivos_a_convertir:
        messagebox.showinfo("Resultado", "No se encontraron archivos compatibles para convertir.")
        return

    carpeta_salida = filedialog.askdirectory(title="Selecciona la carpeta de salida")
    if not carpeta_salida:
        return

    errores = []
    procesados = 0
    for ruta_archivo in archivos_a_convertir:
        try:
            nombre_pdf = ruta_archivo.with_suffix(".pdf").name
            ruta_pdf = Path(carpeta_salida) / nombre_pdf
            convertir_archivo(ruta_archivo, ruta_pdf)
            procesados += 1
        except Exception as error:
            errores.append(f"{ruta_archivo.name}: {error}")

    if errores:
        mensaje = f"Se convirtieron {procesados} archivos correctamente.\n\nErrores:\n" + "\n".join(errores)
        messagebox.showwarning("Conversión parcial", mensaje)
    else:
        messagebox.showinfo("Conversión completada", f"Se convirtieron {procesados} archivos correctamente.")


if __name__ == "__main__":
    main()