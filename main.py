import pygame

from scripts import draw as d

bullets = []
blocks = []
x = 0
wallT = (0,0,600,50)
wallB = (0,550,600,50)
d.createwall(blocks, x, 600, False, True, 0,0,1,50)
d.createwall(blocks, x, 600, False, True, 0,550,1,50)
wallL = (0,0,50,600)
wallR = (550,0,50,600)
d.createwall(blocks, x, 600, True, False, 0,0,50,1)
d.createwall(blocks, x, 600, True, False, 550,0,50,1)

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
        self.dt = 0
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
                    if event.key == pygame.K_SPACE:
                        bullets.append(pygame.Rect(self.player.centerx, self.player.centery-5, 10, 10))
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
            if self.player.colliderect(wallT):
                if self.movement[3]:
                    self.player.y = 50
            if self.player.colliderect(wallB):
                if self.movement[1]:
                    self.player.y = 500
                    
            if self.player.colliderect(wallL):
                if self.movement[0]:
                    self.player.x = 50
            if self.player.colliderect(wallR):
                if self.movement[2]:
                    self.player.x = 500
            for bul in bullets:
                if not bul.collidelistall(blocks):
                    bul.x += 350 * self.dt
            #/CONTROLS
            if self.movement[0]:
                self.player.x -= 350 * self.dt
            if self.movement[1]:
                self.player.y += 350 * self.dt
            if self.movement[2]:
                self.player.x += 350 * self.dt
            if self.movement[3]:
                self.player.y -= 700 * self.dt
            if self.player.bottom <= 550:
                self.player.y += 350 * self.dt
            #/RENDER
            pygame.draw.rect(self.screen, (255, 0, 0), self.player)
            
            for blockf in blocks:
                pygame.draw.rect(self.screen, (255, 255, 255), blockf)

            for buls in bullets:
                pygame.draw.rect(self.screen, (255, 0, 255), buls)
        #/SCRIPTEND
            self.display.flip()
            self.dt = self.clock.tick(60) / 1000


Game().run()