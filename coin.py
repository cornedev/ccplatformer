import pygame

coinframew = 64
coinframeh = 64
coinframecount = 6
coinanimspeed = 0.15

coin = pygame.image.load("gfx/coinspritesheet.png").convert_alpha()

coinframes = []
for i in range(coinframecount):
    coinframe = coin.subsurface(pygame.Rect(i * coinframew, 0, coinframew, coinframeh))
    coinframe = pygame.transform.scale(coinframe, (64, 64))
    coinframes.append(coinframe)