# Example file showing a circle moving on screen
import pygame
# pygame setup
pygame.init()
display = pygame.display
dW = 1280
dH = 720
screen = display.set_mode((dW, dH))
clock = pygame.time.Clock()
running = True
dt = 0
rayCol = (255, 0, 0)
rayRes = 5
rayX = 0
rayY = 0
rayW = rayRes * 10
rayH = rayRes * 10
import functions

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    functions.Raytrace(pygame.draw.rect, screen, rayX, rayY, rayW, rayH, dW, dH, rayRes)
    pygame.draw.rect(screen, rayCol, (rayX, rayY, rayW, rayH))
    # flip() the display to put your work on screen
    display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
