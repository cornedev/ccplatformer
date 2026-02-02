import pygame

def musicstart():
    pygame.mixer.music.load("sfx/lavachicken.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)