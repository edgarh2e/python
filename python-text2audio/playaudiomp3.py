import pygame

# Inicializar el módulo pygame
pygame.init()

# Cargar y reproducir el archivo de audio
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

# Esperar hasta que finalice la reproducción
while pygame.mixer.music.get_busy():
    continue

# Detener el módulo pygame
pygame.quit()

