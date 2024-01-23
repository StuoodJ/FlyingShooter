import pygame
import math
import player
from player import Player
playercon = 5
pygame.init()
display = pygame.display
dW = 1280
dH = 720
screen = display.set_mode([dW, dH])
clock = pygame.time.Clock()
running = True
dt = 0
bW = 50
bH = 50
playercolor = (255, 0, 0)
playerx = dW/2+bW/2
playery = dH/2+bH/2
from player import *
from controls import *

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    keys = pygame.key.get_pressed()
    control(playerx, playery, dt, keys)
    Player(screen, playercolor, playerx, playery, bW, bH, dt)
    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
