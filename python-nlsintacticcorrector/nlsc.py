import nltk

# Descargar los recursos necesarios (ejecutar solo una vez)
import sys

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Leer el archivo de texto
with open(sys.argv[1], 'r') as archivo:
    texto = archivo.read()

# Aplicar el corrector sintáctico
tokens = nltk.word_tokenize(texto)
etiquetas_pos = nltk.pos_tag(tokens)
entidades_nombradas = nltk.ne_chunk(etiquetas_pos)

# Mostrar los resultados
print(entidades_nombradas)

