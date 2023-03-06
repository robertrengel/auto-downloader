import requests
import os
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
import time

carpeta_destino = 'descargas'
enlace = "https://www.mediafire.com/file/30nlysp4x6cdku3/[SoAnime]+M-I-S3-Full-HD-01.mkv/file"

nombre_archivo = enlace.split('/')[-1]

response = requests.get(enlace, stream=True)
# Obtener tamaño del archivo
tamano_archivo = int(response.headers.get('content-length', 0))
# Crear objeto tqdm para mostrar la barra de progreso
barra_progreso = tqdm(total=tamano_archivo, unit='B', unit_scale=True)
# Guardar archivo en la carpeta destino

with open(os.path.join(carpeta_destino, nombre_archivo), 'wb') as f:
    for datos in response.iter_content(chunk_size=1024):
        # Escribir datos en el archivo
        f.write(datos)
        # Actualizar barra de progreso
        
        barra_progreso.update(len(datos))

barra_progreso.close()

# Abre el archivo en modo append
with open('descargados.txt', 'a') as file:
    file.write(nombre_archivo + '\n')
