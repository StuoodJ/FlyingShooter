import pygame
import math
import player
from player import Player
playercon = 5
pygame.init()
display = pygame.display
dW = 550
dH = 550
screen = display.set_mode([dW, dH])
clock = pygame.time.Clock()
running = True
dt = 0
bW = dW//10
bH = dH//10
playercolor = (255, 0, 0)
playerx = dW/2+bW/2
playery = dH/2+bH/2
from player import *
mapWidth = dW//bW   #550/50=11
mapHeight = dH//bH  #550/50=11

gamemap = [1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
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
    if playerx+bW >= dW:
        playerx = dW-bW
    if playerx <= 0:
        playerx = 0
    if playery+bH >= dH:
        playery = dH-bH
    if playery <= 0:
        playery = 0

    def blockcreate(num):
        blockx = 0
        for blockx in range(11*11):
            blockx += 50
        if num == 1:
            pygame.draw.rect(screen, (255,255,255), (gamemap.index(blockx, num), num, bW, bH))
        elif num == 0:
            pygame.draw.rect(screen, (255,0,255), (num.__index__(), num, bW, bH))

        
    blocks = list(map(blockcreate,gamemap))
    
    Player(screen, playercolor, playerx, playery, bW, bH)
    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
