import pygame

from scripts import draw as d

blocks = []
x = 0
d.createwall(blocks, x, 600, False, True, 0, 0, 1, 50)
d.createwall(blocks, x, 600, False, True, 0, 550, 1, 50)

d.createwall(blocks, x, 600, True, False, 0, 0, 50, 1)
d.createwall(blocks, x, 600, True, False, 550, 0, 50, 1)

class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.dW = 600
        self.dH = 600
        self.screen = self.display.set_mode([self.dW, self.dH])
        self.clock = pygame.time.Clock()
        self.movement = [False, False, False, False]
        #/VARIABLES
        self.bW = self.dW//10
        self.bH = self.dH//10
        self.player = pygame.Rect(285, 285, self.bW, self.bH)
        #/WALLFUNCTION
        

#/IMPORTS/RUN
    def run(self):
        while True:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = True
                    if event.key == pygame.K_UP:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = False
                    if event.key == pygame.K_UP:
                        self.movement[3] = False
                        
        #/PLAYERSCRIPT
            #/COLLISIONS
            if self.player.colliderect(0, 0, self.dW, 50):
                if self.movement[3]:
                    self.player.y = 50
            if self.player.colliderect(0, 550, self.dW, 50):
                if self.movement[1]:
                    self.player.y = 550 - self.bW
                    
            if self.player.colliderect(0, 0, 50, self.dH):
                if self.movement[0]:
                    self.player.x = 50
            if self.player.colliderect(550, 0, 50, self.dH):
                if self.movement[2]:
                    self.player.x = 550 - self.bW
            #/CONTROLS
            if self.movement[0]:
                self.player.x -= 350 * self.dt
            if self.movement[1]:
                self.player.y += 350 * self.dt
            if self.movement[2]:
                self.player.x += 350 * self.dt
            if self.movement[3]:
                self.player.y -= 350 * self.dt
            #/RENDER
            pygame.draw.rect(self.screen, (255, 0, 0), self.player)

            for blockf in blocks:
                pygame.draw.rect(self.screen, (255, 255, 255), blockf)
        #/SCRIPTEND
            self.display.flip()
            self.dt = self.clock.tick(60) / 1000


Game().run()