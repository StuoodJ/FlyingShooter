import pygame

def createwall(list, block, len, ve, ho, x, y, wd, hg):
    for _ in range(len):
        block = pygame.Rect(x, y, wd, hg)
        list.append(block)
        if ho is True:
            x += wd
        elif ve is True:
            y += hg