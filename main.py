import pygame
import math
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
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    mousepos = pygame.mouse.get_pos()
    mousex = mousepos[0]
    mousey = mousepos[1]
    blockx = mousex-bW/2
    blocky = mousey-bH/2
    pygame.draw.rect(screen, (255,0,0), (blockx, blocky, bW, bH))
    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
