import pygame
import Raytracerinprogress as r

def Raytrace():
    if r.rayX < r.dW - 9:
        brx = r.rayX
        bry = r.rayY
        pygame.draw.rect(r.screen, (255, 255, 255), (brx, bry, r.rayW, r.rayH))
        r.rayX += r.rayRes * 10
    elif r.rayX >= r.dW:
        r.rayX = 0
        r.rayY += r.rayRes * 10
    elif r.rayY >= r.dH:
        r.rayY = 0
        r.rayX = 0