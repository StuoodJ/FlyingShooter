import pygame

def Player(screen, playercolor, playerx, playery, bW, bH, dt, Xcon, Ycon):
    #playercode
    if Xcon > 0:
        #Right
        playerx += 350 * dt
        return playerx
    if Xcon < 0:
        #left
        playerx -= 350 * dt
        return playerx
    if Ycon < 0:
        #Up
        playery -= 350 * dt
        return playery
    if Ycon > 0:
        #Down
        playery += 350 * dt
        return playery
    playerrect = (playerx, playery, bW, bH)
    #playerdraw
    pygame.draw.rect(screen, playercolor, playerrect)
