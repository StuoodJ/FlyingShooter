import pygame
def Player(screen, playercolor, playerx, playery, bW, bH, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerx -= 350 * dt
    if keys[pygame.K_RIGHT]:
        playerx += 350 * dt
    if keys[pygame.K_UP]:
        playery -= 650 * dt
    if keys[pygame.K_DOWN]:
        playery += 650 * dt  
    playerrect = (playerx, playery, bW, bH)
    pygame.draw.rect(screen, playercolor, playerrect)
    