import pygame

def control(Xcon, Ycon, keys):
#Xcontrols
    if keys[pygame.K_LEFT]:
        Xcon = -1
        return Xcon
    elif keys[pygame.K_RIGHT]:
        Xcon = 1
        return Xcon
    else:
        Xcon = 0
#Ycontrols
    if keys[pygame.K_UP]:
        Ycon = -1
        return Ycon
    elif keys[pygame.K_DOWN]:
        Ycon = 1
        return Ycon
    else:
        Ycon = 0
