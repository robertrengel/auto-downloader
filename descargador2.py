import requests
import time
from tqdm import tqdm
import os

carpeta_destino = 'descargas'

enlace = "https://aprendepython.es/_downloads/907b5202c1466977a8d6bd3a2641453f/aprendepython.pdf"

nombre_archivo = enlace.split('/')[-1]

response = requests.get(enlace, stream=True)
# Obtener tamaño del archivo
tamano_archivo = int(response.headers.get('content-length', 0))
# Crear objeto tqdm para mostrar la barra de progreso
barra_progreso = tqdm(total=tamano_archivo, unit='B', unit_scale=True)
# Guardar archivo en la carpeta destino

with open(os.path.join(carpeta_destino, nombre_archivo), 'wb') as f:
    for datos in response.iter_content(chunk_size=1024):
        print()
        print(response.status_code)
        print()
        # Escribir datos en el archivo
        f.write(datos)
        # Actualizar barra de progreso
        
        barra_progreso.update(len(datos))
# Cerrar la barra de progreso
    #f.flush()
    #response.close()
    time.sleep(10)
    print("despues del tiempo")
    print(response.status_code)
    print()
barra_progreso.close()