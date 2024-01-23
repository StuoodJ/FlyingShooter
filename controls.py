import pygame

def control(Xcon, Ycon, keys):
#Xcontrols
    if keys[pygame.K_LEFT]:
        Xcon = -1
        return Xcon
    if keys[pygame.K_RIGHT]:
        Xcon = 1
        return Xcon
    if keys[pygame.K_UP]:
        Ycon = -1
        return Ycon
    if keys[pygame.K_DOWN]:
        Ycon = 1
        return Ycon
