import pygame

def Player(screen, playercolor, playerx, playery, bW, bH):
    #playercode


    playerrect = (playerx, playery, bW, bH)
    #playerdraw
    pygame.draw.rect(screen, playercolor, playerrect)
