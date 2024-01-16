# Example file showing a circle moving on screen
import pygame
# pygame setup
pygame.init()
import functions
from functions import *
clock = pygame.time.Clock()
running = True
dt = 0
rayCol = (255, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    Raytrace()
    pygame.draw.rect(screen, rayCol, (rayX, rayY, rayW, rayH))
    # flip() the display to put your work on screen
    display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
