import pyttsx3
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',0.9)    # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice
idx = 0
for voice in voices:
    print (voice)
    print (idx)
    idx = idx+1
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[85].id)   #changing index, changes voices. 1 for female

engine.say("Hola a todos, esto es una  prueba para convertir texto a audio, o no?")
engine.say('Mi velocidad actual es ' + str(rate))
engine.say("Hola Judith fea")
engine.runAndWait()
engine.stop()

# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
