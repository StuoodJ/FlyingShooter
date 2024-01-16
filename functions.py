import pygame
from Raytracerinprogress import *

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