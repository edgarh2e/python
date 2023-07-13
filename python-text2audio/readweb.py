import requests
import sys
from txt2speech import Txt2speech
from bs4 import BeautifulSoup

argumentos = sys.argv

url = argumentos[1]

print(url)
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
texto = soup.get_text()
Txt2speech.speech(texto.replace("\n", " ").replace("\r", " ").replace("\t", " "))

# Procesa y manipula el texto
print(texto)

