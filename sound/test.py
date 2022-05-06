import pygame

pygame.mixer.init(44200)
pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.load('3.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
