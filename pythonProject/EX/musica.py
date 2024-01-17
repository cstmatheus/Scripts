import pygame

z = 1

while z != 0:
    pygame.init()
    pygame.mixer.music.load('ex02.mp3')
    pygame.mixer.music.play()

    z = int(input('algo'))