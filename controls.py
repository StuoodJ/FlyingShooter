import pygame

Xcon = 0
Ycon = 0
def control():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        Xcon = -1
    elif keys[pygame.K_RIGHT]:
        Xcon = 1
    else:
        Xcon = 0

    if keys[pygame.K_UP]:
        Ycon = -1
    elif keys[pygame.K_DOWN]:
        Ycon = 1
    else:
        Ycon = 0