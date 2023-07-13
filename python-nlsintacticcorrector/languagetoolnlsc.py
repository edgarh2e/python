import sys
from language_tool_python import LanguageTool


class Correcttxt:

    def __init__(self):
        self.arg=""

    def correct(txt_file):
        with open(txt_file, 'r') as archivo:
            texto = archivo.read()

        # Crea una instancia de LanguageTool
        tool = LanguageTool('es-MX')  

        errores = tool.check(texto)
        correcciones = tool.correct(texto)
        # corregido = LanguageTool.correct(texto, correcciones)
        # Imprime los errores y sugerencias
        for error in errores:
            print(error)
        
        # print(texto_corregido)
        print(correcciones)
        return correcciones

