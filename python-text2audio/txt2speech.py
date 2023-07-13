from gtts import gTTS

class Txt2speech:

    def __init__(self):# method
        self.arg = ""

    def speech(txt):
        # Texto que deseas convertir a audio
        # archivo = open(txt, 'a')
        # contenido = archivo.read()
        # archivo.close()
        # Crear instancia de gTT[[S
        print(txt)
        tts = gTTS(text=txt, lang='es')
        # Guardar el archivo de audio
        tts.save('audio.mp3')
        print(tts)




