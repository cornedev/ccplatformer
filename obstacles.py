import pygame

def floorcreate(floor, floorx, floory, floorw, floorh):
    floorimg = pygame.transform.scale(floor, (floorw, floorh))
    floorrect = floorimg.get_rect(topleft=(floorx, floory))
    return (floorimg, floorrect)

def coincreate(coin, coinx, coiny):
    coinimg = pygame.transform.scale(coin, (64, 64))
    coinrect = coinimg.get_rect(topleft=(coinx, coiny))
    return (coinimg, coinrect)
