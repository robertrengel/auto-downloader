import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def open_browser(url):

   os.environ['PATH'] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
   options = webdriver.ChromeOptions()
   service = ChromeService(executable_path=os.environ['PATH'])
   driver = webdriver.Chrome(options=options)
   driver = webdriver.Chrome(service=service, options=options)

   # Página web que contiene el botón de descarga
   #url = 'https://www.mediafire.com/file/gxb1uwd4aggyv42/[SoAnime]+M-I-S3-Full-HD-03.mkv/file'

   # Cargar la página web en el navegador
   driver.implicitly_wait(10)
   driver.get(url)
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
   return enlace_link_url
