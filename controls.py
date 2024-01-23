import pygame

def control(playerx, playery, dt, keys):
#Xcontrols
    if keys[pygame.K_LEFT]:
        #Lef
        playerx -= 350 * dt
        return control.__get__(playerx)
    if keys[pygame.K_RIGHT]:
        #Right
        playerx += 350 * dt
        return control.__get__(playerx)
    if keys[pygame.K_UP]:
        #Up
        playery -= 350 * dt
        return control.__get__(playery)
    if keys[pygame.K_DOWN]:
        #Down
        playerx += 350 * dt
        return control.__get__(playery)
