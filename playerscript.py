import pygame

def Player(screen, playercolor, playerx, playery, bW, bH):
    #playercode
    playerrect = (playerx, playery, bW, bH)
    #playerdraw
    player = pygame.draw.rect(screen, playercolor, playerrect)
    return player