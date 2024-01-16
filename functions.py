import pygame

display = pygame.display
dW = 1280
dH = 720
screen = display.set_mode((dW, dH))
rayRes = 5
rayX = 0
rayY = 0
rayW = rayRes * 10
rayH = rayRes * 10

def Raytrace():
    if rayX < dW - 9:
        brx = rayX
        bry = rayY
        pygame.draw.rect(screen, (255, 255, 255), (brx, bry, rayW, rayH))
        rayX += rayRes * 10
    elif rayX >= dW:
        rayX = 0
        rayY += rayRes * 10
    elif rayY >= dH:
        rayY = 0
        rayX = 0