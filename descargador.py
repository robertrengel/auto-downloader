import requests
import os
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService



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

#lista_descargados = descargados()
# Lista de enlaces
#enlaces = ['https://download1650.mediafire.com/ug8paf5phkegdm1ZVXohMHMea1zKdiBFIUaXKqbXlgk168zbFGJUI1V7B5ltud_Ci52_mcsNub-9ephaJVmxr3kAbQ/nzwtxlv7p9i70ay/%5BSoAnime%5D+M-I-S3-Full-HD-02.mkv']

# Carpeta donde se guardarán los archivos descargados

# Si la carpeta no existe, se crea
for enlace in enlaces_paginas_descargar:
    os.environ['PATH'] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=os.environ['PATH'])
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get(enlace)
    print("despues del drive.get")
   # Esperar hasta que se cargue el elemento
    element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//a[@id='downloadButton']"))
    )
   # Esperar a que se cargue el botón de descarga (cambiar el selector según corresponda)
    boton_descarga = driver.find_element(By.XPATH, "//a[@id='downloadButton']")
    enlace_link_url = boton_descarga.get_attribute("href")
    print(enlace_link_url)
   # Cerrar el navegador web
    driver.quit()
    #url = open_browser(enlace)
    #descargador(url)
    
    nombre_archivo = enlace_link_url.split('/')[-1]
    print(nombre_archivo)
    print()
    if nombre_archivo in lista_descargados:
        print()
        print("el archivo" + nombre_archivo + " ya se encuentra descargado")
        print()
        continue
    
    # Descargar archivo
       
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
    # Cerrar la barra de progreso
    barra_progreso.close()

    # Abre el archivo en modo append
    with open('descargados.txt', 'a') as file:
        file.write(nombre_archivo + '\n')

