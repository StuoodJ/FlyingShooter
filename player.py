import pygame
def Player(screen, playercolor, playerx, playery, bW, bH):
    playerrect = (playerx, playery, bW, bH)
    pygame.draw.rect(screen, playercolor, playerrect)
    