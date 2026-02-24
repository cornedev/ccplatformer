import pygame

goombaframew = 64
goombaframeh = 64
goombaframecount = 2
goombaanimspeed = 0.1

goomba = pygame.image.load("gfx/goombaspritesheet_walk.png").convert_alpha()
goombakilled = pygame.image.load("gfx/goombaspritesheet_killed.png").convert_alpha()

goombaframes = []
for i in range(goombaframecount):
    goombaframe = goomba.subsurface(pygame.Rect(i * goombaframew, 0, goombaframew, goombaframeh))
    goombaframe = pygame.transform.scale(goombaframe, (64, 64))
    goombaframes.append(goombaframe)

def goombacreate(goomba, goombax, goombay):
    goombaimg = pygame.transform.scale(goomba, (64, 64))
    goombarect = goombaimg.get_rect(topleft=(goombax, goombay))
    return {"goombaimg": goombaimg, "goombarect": goombarect, "goombavelx": -2, "goombavely": 0, "ground": False}

def goombaupdate(goomba, floors):
    goomba["goombarect"].x += goomba["goombavelx"]

    for _, floorrect in floors:
        if goomba["goombarect"].colliderect(floorrect):
            if goomba["goombavelx"] > 0:
                goomba["goombarect"].right = floorrect.left
            else:
                goomba["goombarect"].left = floorrect.right
            goomba["goombavelx"] *= -1

    goomba["goombavely"] += 0.5
    goomba["goombarect"].y += goomba["goombavely"]
    goomba["ground"] = False

    for _, floorrect in floors:
        if goomba["goombarect"].colliderect(floorrect):
            if goomba["goombavely"] > 0:
                goomba["goombarect"].bottom = floorrect.top
                goomba["goombavely"] = 0
                goomba["ground"] = True