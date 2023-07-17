import cv2
import pytesseract

# Configuración de Tesseract (ruta al ejecutable tesseract)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Ruta real al ejecutable en tu sistema

# Carga la imagen
imagen = cv2.imread('img.jpg')  # Reemplaza 'imagen.jpg' con el nombre o ruta de tu imagen

# Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplica un umbral para resaltar el texto
_, imagen_umbral = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# Extrae el texto de la imagen utilizando pytesseract
texto_extraido = pytesseract.image_to_string(imagen_umbral)

# Guarda el texto en un archivo de texto
with open('xtrac_txt.txt', 'w') as archivo:
    archivo.write(texto_extraido)

