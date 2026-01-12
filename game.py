import pygame
import sys

pygame.init()

gamew = 1000
gameh = 700

gamescreen = pygame.display.set_mode((gamew, gameh))
gameicon = pygame.image.load("gfx/icon.png").convert_alpha()
pygame.display.set_icon(gameicon)
pygame.display.set_caption("ccplatformer")
gameclock = pygame.time.Clock()
gamefps = 60

player = pygame.image.load("gfx/player.png").convert_alpha()
playerw = 128
playerh = 128
playerx = 200
playery = 200
player = pygame.transform.scale(player, (playerw, playerh))
playerrect = player.get_rect(topleft=(playerx, playery))
playerspeed = 5
playergravity = 1
playervely = 0
playerjump = -18

floor = pygame.image.load("gfx/floor.png").convert_alpha()
def floorcreate(floorx, floory, floorw, floorh):
    floorimg = pygame.transform.scale(floor, (floorw, floorh))
    floorrect = floorimg.get_rect(topleft=(floorx, floory))
    return (floorimg, floorrect)

floors = [
    floorcreate(400, 400, 1000, 100),
    floorcreate(200, 500, 1000, 100),
    floorcreate(200, 600, 1000, 100)
]

white = (255, 255, 255)
blue = (135, 206, 235)

ground = True
gamerunning = True

while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
   
    gamedx = 0
    gameinput = pygame.key.get_pressed()
    if gameinput[pygame.K_a]:
        gamedx = -playerspeed
    if gameinput[pygame.K_d]:
        gamedx = playerspeed
    playerrect.x += gamedx

    for floorimg, floorrect in floors:
        if playerrect.colliderect(floorrect):
            if gamedx > 0:
                playerrect.right = floorrect.left
            if gamedx < 0:
                playerrect.left = floorrect.right
    if gameinput[pygame.K_SPACE] and ground:
        playervely = playerjump
        ground = False

    playervely += playergravity
    playerrect.y += playervely
    ground = False
    for floorimg, floorrect in floors:
        if playerrect.colliderect(floorrect):
            if playervely > 0:
                playerrect.bottom = floorrect.top
                playervely = 0
                ground = True
            elif playervely < 0:
                playerrect.top = floorrect.bottom
                playervely = 0

    gamescreen.fill(blue)
    gamescreen.blit(player, playerrect)
    for floorimg, floorrect in floors:
        gamescreen.blit(floorimg, floorrect)

    pygame.display.flip()
    gameclock.tick(gamefps)

pygame.quit()
sys.exit()
