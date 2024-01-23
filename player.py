import pygame
from controls import Xcon, Ycon
def Player(screen, playercolor, playerx, playery, bW, bH, dt):
    playerrect = (playerx, playery, bW, bH)
    #playercode
    if Xcon > 0:
        #Right
        playerx += 350 * dt
    elif Xcon < 0:
        #left
        playerx -= 350 * dt
    elif Ycon < 0:
        #Up
        playery -= 350 * dt
    elif Ycon > 0:
        #Down
        playery += 350 * dt
    #playerdraw
    pygame.draw.rect(screen, playercolor, playerrect)
