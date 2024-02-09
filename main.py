import pygame
import math
playercon = 5
pygame.init()
display = pygame.display
dW = 600
dH = 600
screen = display.set_mode([dW, dH])
clock = pygame.time.Clock()
running = True
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
#/IMPORTS/RUN
from playerscript import *

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(black)
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
#/COLLISIONS
    if playerx+bW >= dW:
        playerx = dW-bW
    if playerx <= 0:
        playerx = 0
    if playery+bH >= dH:
        playery = dH-bH
    if playery <= 0:
        playery = 0
#/RENDERMAP
    def blockcreate(screen, x, y, blockwidth, blockheight, color):
        r = pygame.Rect(x, y, blockwidth, blockheight)
        rd = pygame.draw.rect(screen, color, r)
        
        

#/RENDERMISC
    blockcreate(screen, 0, 0, bW, bH, white)
    blockcreate(screen, 70, 0, bW, bH, white)
    Player(screen, playercolor, playerx, playery, bW, bH)
    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
