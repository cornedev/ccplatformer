import pygame
import sys

pygame.init()

gamew = 1000
gameh = 700

gamescreen = pygame.display.set_mode((gamew, gameh))
pygame.display.set_caption("ccplatformer")
gameclock = pygame.time.Clock()
gamefps = 60

player = pygame.image.load("gfx/player.png").convert_alpha()
playerw = 200
playerh = 200
playerx = 200
playery = 200
player = pygame.transform.scale(player, (playerw, playerh))
playerrect = player.get_rect(topleft=(playerx, playery))
playerspeed = 5

white = (255, 255, 255)
blue = (135, 206, 235)

gamerunning = True

while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
    
    gameinput = pygame.key.get_pressed()
    if gameinput[pygame.K_w]:
        playerrect.y -= playerspeed
    if gameinput[pygame.K_s]:
        playerrect.y += playerspeed
    if gameinput[pygame.K_a]:
        playerrect.x -= playerspeed
    if gameinput[pygame.K_d]:
        playerrect.x += playerspeed

    gamescreen.fill(blue)
    gamescreen.blit(player, playerrect)

    pygame.display.flip()
    gameclock.tick(gamefps)

pygame.quit()
sys.exit()