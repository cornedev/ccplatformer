import pygame

def musicstart():
    pygame.mixer.music.load("sfx/lavachicken.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

audiojump = pygame.mixer.Sound("sfx/jump.mp3")
audiojump.set_volume(0.5)
audiocoin = pygame.mixer.Sound("sfx/coin.mp3")
audiocoin.set_volume(0.5)

def playerjumpsfx():
    audiojump.play()

def playercoinsfx():
    audiocoin.play()

musicrunning = True
