import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')#arquivo inexiste, apenas para teste do código
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()