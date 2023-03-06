import os
import time
import cfscrape
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

carpeta_destino = 'descargas'

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
    
#cargar_enlaces_paginas_descargar
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
with open(file_path, 'r') as f:
    enlaces = f.read()
    f.close()
enlaces_paginas_descargar = enlaces.split('\n')
print(enlaces_paginas_descargar)

with open("descargados.txt", 'r') as f:
    archivos_descargados = f.read()
    f.close()
    
lista_descargados = archivos_descargados.split('\n')
print(lista_descargados)


#for enlace in enlaces_paginas_descargar:
enlace = enlaces_paginas_descargar[0]    
scraper = cfscrape.create_scraper()
response = scraper.get(enlace)
#response = requests.get(url)
print()
print(response.status_code)
print()

soup = BeautifulSoup(response.content, 'html.parser')
element = soup.find('a', id='downloadButton')
enlace_link_url = element['href']
nombre_archivo = enlace_link_url.split('/')[-1]
print()
print(nombre_archivo)
print()

# if nombre_archivo in lista_descargados:
#     print()
#     print("el archivo " + nombre_archivo + " ya se encuentra descargado")
#     print()
#     exit()

# Descargar archivo
    
response = scraper.get(enlace, stream=True)
# Obtener tamaño del archivo
tamano_archivo = int(response.headers.get('content-length', 0))
# Crear objeto tqdm para mostrar la barra de progreso
#barra_progreso = tqdm(total=tamano_archivo, unit='B', unit_scale=True)
# Guardar archivo en la carpeta destino
# downloaded_size = 0
with open(os.path.join(carpeta_destino, nombre_archivo), 'wb') as f:
    for datos in response.iter_content(chunk_size=1024):
        # print()
        # print(response.raise_for_status)
        # print()
        # downloaded_size += len(datos)
        # Escribir datos en el archivo
        f.write(datos)
        # Actualizar barra de progreso
        
        # barra_progreso.update(len(datos))
# while True:
#     print(tamano_archivo)
#     print(downloaded_size)
#     time.sleep(2)
    
#barra_progreso.close()

# Abre el archivo en modo append
with open('descargados.txt', 'a') as file:
    file.write(nombre_archivo + '\n')
