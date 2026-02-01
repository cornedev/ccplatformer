import pygame
import sys

from obstacles import floorcreate, coincreate

pygame.init()

gamew = 1000
gameh = 700

gamescreen = pygame.display.set_mode((gamew, gameh))
gameicon = pygame.image.load("gfx/icon.png").convert_alpha()
pygame.display.set_icon(gameicon)
pygame.display.set_caption("ccplatformer")
gameclock = pygame.time.Clock()
gamefps = 60

camerax = 0
cameray = 0

worldw = 4000
worldh = 2000

playersheet = pygame.image.load("gfx/playerspritesheet_walk_idle.png").convert_alpha()
playerframew = 32
playerframeh = 64
playerw = 64
playerh = 128
playerx = 200
playery = 200
playerframecount = 4

playerframes = []
for i in range(playerframecount):
    playerframe = playersheet.subsurface(
        pygame.Rect(i * playerframew, 0, playerframew, playerframeh)
    )
    playerframe = pygame.transform.scale(playerframe, (playerw, playerh))
    playerframes.append(playerframe)

player = playerframes[0]
playerrect = player.get_rect(topleft=(playerx, playery))
playerspeed = 5
playergravity = 1
playervely = 0
playerjumpstrength = -18
playerframeindex = 0
playeranimspeed = 0.15
playercrouch = pygame.image.load("gfx/playerspritesheet_crouch.png").convert_alpha()
playercrouchframe = pygame.transform.scale(playercrouch, (playerw, playerh))
playerjump = pygame.image.load("gfx/playerspritesheet_jump.png").convert_alpha()
playerjumpframe = pygame.transform.scale(playerjump, (playerw, playerh))

floor = pygame.image.load("gfx/floor.png").convert_alpha()
floors = [
    floorcreate(floor, 0, 600, 4000, 100),
    floorcreate(floor, 600, 450, 800, 100),
    floorcreate(floor, 1600, 350, 800, 100),
]

coin = pygame.image.load("gfx/coinspritesheet.png").convert_alpha()
coinframew = 64
coinframeh = 64
coinframecount = 6
coinanimspeed = 0.15

coinframes = []
for i in range(coinframecount):
    coinframe = coin.subsurface(pygame.Rect(i * coinframew, 0, coinframew, coinframeh))
    coinframe = pygame.transform.scale(coinframe, (64, 64))
    coinframes.append(coinframe)

coins = [
    {"rect": coincreate(coinframes[0], 300, 300)[1], "coinframeindex": 0},
]

white = (255, 255, 255)
blue = (135, 206, 235)

ground = True
playerright = True
gamerunning = True

while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
   
    gamedx = 0
    gameinput = pygame.key.get_pressed()
    
    if gameinput[pygame.K_a]:
        playerright = False
    if gameinput[pygame.K_d]:
        playerright = True

    if not (gameinput[pygame.K_s] and ground):
        if gameinput[pygame.K_a]:
            gamedx = -playerspeed
        if gameinput[pygame.K_d]:
            gamedx = playerspeed
    playerrect.x += gamedx
    
    if not ground:
        player = playerjumpframe
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    elif gameinput[pygame.K_s] and ground:
        player = playercrouchframe
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    elif gamedx != 0:
        playerframeindex += playeranimspeed
        if playerframeindex >= len(playerframes):
            playerframeindex = 0
        player = playerframes[int(playerframeindex)]
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    else:
        playerframeindex = 0
        player = playerframes[0]
        if not playerright:
            player = pygame.transform.flip(player, True, False)

    for floorimg, floorrect in floors:
        if playerrect.colliderect(floorrect):
            if gamedx > 0:
                playerrect.right = floorrect.left
            if gamedx < 0:
                playerrect.left = floorrect.right
    if gameinput[pygame.K_SPACE] and ground:
        playervely = playerjumpstrength
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

    camerax = playerrect.centerx - gamew // 2
    camerax = max(0, min(camerax, worldw - gamew))

    gamescreen.fill(blue)
    gamescreen.blit(player, (playerrect.x - camerax, playerrect.y - cameray))

    coins = [coin for coin in coins if not playerrect.colliderect(coin["rect"])]
    for coin in coins:
        coin["coinframeindex"] += coinanimspeed
        if coin["coinframeindex"] >= len(coinframes):
            coin["coinframeindex"] = 0

        coincurrentframe = coinframes[int(coin["coinframeindex"])]
        gamescreen.blit(coincurrentframe, (coin["rect"].x - camerax, coin["rect"].y - cameray))

    for floorimg, floorrect in floors:
        gamescreen.blit(floorimg, (floorrect.x - camerax, floorrect.y - cameray))
    pygame.display.flip()
    gameclock.tick(gamefps)

pygame.quit()
sys.exit()
