import requests
from bs4 import BeautifulSoup

# Página web que contiene el botón de descarga
url = 'https://www.mediafire.com/file/gxb1uwd4aggyv42/[SoAnime]+M-I-S3-Full-HD-03.mkv/file'

# Obtener el contenido HTML de la página web
response = requests.get(url)
contenido = response.content

# Crear un objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(contenido, 'html.parser')
print(soup.prettify())
# Buscar el botón de descarga por su clase o identificador
boton_descarga = soup.find('a', {'class': 'input popsok'})
print(boton_descarga)

# Obtener el atributo href del botón de descarga
enlace_descarga = boton_descarga.get('href')

# Imprimir el enlace de descarga
print(enlace_descarga)
