import pygame

def createwall(list, block, length, vertical, horizontal, x, y, width, height):
    for _ in range(length):
        block = pygame.Rect(x, y, width, height)
        list.append(block)
        if horizontal is True:
            x += width
        elif vertical is True:
            y += height