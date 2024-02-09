import pygame
import math
import random
playercon = 5
pygame.init()
display = pygame.display
dW = 600
dH = 600
screen = display.set_mode([dW, dH])
clock = pygame.time.Clock()

#/VARIABLES
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
dt = 0
bW = dW//10
bH = dH//10
playercolor = red
playerx = dW/2+bW/2
playery = dH/2+bH/2
#/WALLFUNCTION
blocks = []
x = 0
def createwall(length,vertical, horizontal, x, y, width, height):
    for _ in range(length):
        block = pygame.Rect(x,y, width, height)
        blocks.append(block)
        if horizontal is True:
            x += width
        elif vertical is True:
            y += height
createwall(dH, True, False, 0, 0, 1, 1)
createwall(dW, False, True, 0, 0, 1, 1)
createwall(dH, True, False, dW-1, 0, 1, 1)
createwall(dW, False, True, 0, dH-1, 1, 1)
#/IMPORTS/RUN
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(black)
#/PLAYERSCRIPT
    #/COLLISIONS
    player = pygame.Rect(playerx, playery, bW, bH)
    if player.collidelistall(blocks):
        playercolor = green
    else:
        playercolor = red
    #/CONTROLS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        #Left
        playerx -= 350 * dt
    if keys[pygame.K_RIGHT]:
        #Right
        playerx += 350 * dt
    if keys[pygame.K_UP]:
        #Up
        playery -= 350 * dt
    if keys[pygame.K_DOWN]:
        #Down
        playery += 350 * dt

#/RENDER
    pygame.draw.rect(screen, playercolor, player)

    for blockf in blocks:
        pygame.draw.rect(screen, white, blockf)
#/SCRIPTEND
    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
