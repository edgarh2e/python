# Almacear,  Procesar/Transformar y Transmitir información es un proceso complejo que al día de hoy y a pesar de todas las herramientas que tenemos, aún es complejo y en algunos casos sensible a "perdida" o corrupción


## Notas de interés: 

[Sci-Hub](https://es.wikipedia.org/wiki/Sci-Hub)

[Presa de la mula](https://www.google.com/search?q=presa+de+la+mula&tbm=isch&chips=q:presa+de+la+mula,online_chips:pinturas+rupestres:Is_k7Ghz4YA%3D&hl=es-419&sa=X&ved=2ahUKEwjx-5DxpLGCAxXxPN4AHRb3B6EQ4lYoAnoECAEQMw&biw=1680&bih=965)

[Solsticio boca de potreritos](https://www.google.com/search?q=solsticio+boca+de+potreritos&sca_esv=580046813&tbm=isch&sxsrf=AM9HkKmWHtjUNgXNxGrwaZZcRBJ46ECIJg:1699339602812&source=lnms&sa=X&ved=2ahUKEwjnioOrpbGCAxWplWoFHdtUAR4Q_AUoAXoECAEQAw&biw=1680&bih=965&dpr=2) 


# Idea inicial

## Todo surgio a partir de querer procesar algunos tipos de datos de entrada como imagenes, texto y audio para convertirlos en archivos de información; información que podría ser manipulada para obtener diferentes formatos de salida, texto y voz pricipalmente, con su respectiva correción e incluso, pero máscompleja, traducción a diferentes lenguajes.

## Uno de los objetivos es digitalizar la mayor cantidad de fuentes de datos o recursos personales, entre los que destacan apuntes, grabaciones o textos, que fueran de interes para su posterior transformación y publicación (en caso de representar una idea que se desea transmitir).

## Estos recursos e información se plantea subir mediante una NAS que por sus siglas en ingles significa Network Attached Storage (Almacenamiento Conectado a la Red).

> NAS: Dispositivo de almacenamiento de datos conectado a una red que permite a los usuarios almacenar y compartir archivos y datos con otros usuarios y dispositivos a través de la red local.

---



**Basicamente esto requeria generar algunos scripts para comenzar a expermientar un poco con algunas librerias y la recomendación inicial fue el uso de pyhton como lenguaje de programación y uso de algunas librerias.**



*Y una de las preguntas inciales:*



> Como convierto texto en audio?



Basicamente con:

  * Software de Texto a Voz (TTS)
  * Aplicaciones en línea (Text2Speech.org, NaturalReaders y TTSReader)
  * Programación (pyttsx3)


## Scripts:


```python
import pyttsx3


# Crear objeto de la clase Text-to-Speech
engine = pyttsx3.init()

# Ingresar el texto que deseas convertir a audio
texto = "Hola, ¿cómo estás?"

# Convertir el texto a voz
engine.say(texto)
engine.runAndWait()

```

[pyttsx3](https://github.com/edgarh2e/python/blob/20231106_presentacion/python-text2audio/text2audio.py)

[repositorio](https://github.com/edgarh2e/python/tree/20231106_presentacion/python-text2audio)

# Pero ahora las cosas se complicaban un poco...

## Ya no solo era necesario converir texto a  audio, si no que se hacia necesario 

   * generar y ejecutar un corrector sintáctico sobre un archivo de texto plano
     ```python
     import nltk
     # Descargar los recursos necesarios (ejecutar solo una vez)
     nltk.download('punkt')
     nltk.download('averaged_perceptron_tagger')
     nltk.download('maxent_ne_chunker')
     nltk.download('words')
    
     # Leer el archivo de texto
     with open('archivo.txt', 'r') as archivo:
        texto = archivo.read()
    
     # Aplicar el corrector sintáctico
     tokens = nltk.word_tokenize(texto)
     etiquetas_pos = nltk.pos_tag(tokens)
     entidades_nombradas = nltk.ne_chunk(etiquetas_pos)
    
     # Mostrar los resultados
     print(entidades_nombradas)
     ```
   * transformar una imagen con texto a un archivo de texto
     ```python
     import cv2
     import pytesseract
    
     # Configuración de Tesseract (ruta al ejecutable tesseract)
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ruta real al ejecutable en tu sistema
    
     # Carga la imagen
     imagen = cv2.imread('imagen.jpg')  # Reemplaza 'imagen.jpg' con el nombre o ruta de tu imagen
    
     # Convierte la imagen a escala de grises
     imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
     # Aplica un umbral para resaltar el texto
     _, imagen_umbral = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
     # Extrae el texto de la imagen utilizando pytesseract
     texto_extraido = pytesseract.image_to_string(imagen_umbral)
    
     # Guarda el texto en un archivo de texto
     with open('texto_extraido.txt', 'w') as archivo:
         archivo.write(texto_extraido)
     ```
   * convertir audio a texto
     ```python
     import speech_recognition as sr

     def convertir_audio_a_texto(nombre_archivo):
         r = sr.Recognizer()
    
         with sr.AudioFile(nombre_archivo) as fuente_audio:
            audio = r.record(fuente_audio)
        
         texto = r.recognize_google(audio, language="es-ES")  # Reemplaza "es-ES" con el idioma adecuado
    
         return texto
    
     nombre_archivo_audio = "audio.wav"  # Reemplaza "audio.wav" con el nombre o ruta del archivo de audio
     texto_convertido = convertir_audio_a_texto(nombre_archivo_audio)

     print(texto_convertido)

     ```
     
[nlsintacticcorrector](https://github.com/edgarh2e/python/tree/20231106_presentacion/python-nlsintacticcorrector)

[img2txt](https://github.com/edgarh2e/python/tree/20231106_presentacion/python-img2txt)


## Y en este punto surge un reto adicional...

### Y si quisiera tomar textos o audios en otro lenguaje y traducirlos o digitalizarlos

> Aquí se parte la idea principal en dos para dar paso a una nueva idea, antes de continuar con la infraestructura y los scripts,
> era necesario conocer el lenguaje que se buscaba digitalizar.
> Por lo que se opta por conocer un nuevo lenguaje
