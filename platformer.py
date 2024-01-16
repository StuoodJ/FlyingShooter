# Example file showing a circle moving on screen
import pygame
# pygame setup
pygame.init()
display = pygame.display
screen = display.set_mode([1280, 720])
clock = pygame.time.Clock()
running = True
dt = 0
pC = (255, 0, 0)
pX = 0
toppY = 0
pW = 50
pH = 50
floorX = 0
floorY = 500
floorW = 1280
floorH = 220
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, pC, (pX, toppY, pW, pH))
    floor = pygame.draw.rect(screen, (255, 255, 255), (floorX, floorY, floorW, floorH))
    bottompY = toppY + pH
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        toppY -= 300 * dt
    elif bottompY < floorY:
        toppY += 30
        
    if keys[pygame.K_LEFT]:
        pX -= 300 * dt
    if keys[pygame.K_RIGHT]:
        pX += 300 * dt


    

    if bottompY >= floorY:
        toppY = 500 - pH




    display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
