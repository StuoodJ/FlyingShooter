import pygame
import random

pygame.init()
width = 800
height = 600
game_display = pygame.display.set_mode((width, height), 0, 400)
pygame.display.set_caption('Color Match')
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
player_size = 50
player_x = width / 2 - player_size / 2
player_y = height - 2 * player_size
player_color = (255, 0, 0)
object_size = 50
object_x = random.randint(0, width - object_size)
object_y = 0
object_speed = 5
randR = random.randint(0, 255)
if randR > 122.5:
    randR=255
elif randR < 122.5:
    randR=0 

if randR == 0:
    randG=random.randint(0, 255)
    if randG > 122.5:
        randG=255
    elif randG < 122.5:
        randG=0 
else:
    randG=0

if randG==0:
    randB=random.randint(0, 255)
    if randB > 122.5:
        randB=255
    elif randB < 122.5:
        randB=0 
R = randR
G = randG
B = randB
object_color = (R, G, B)
score = 0
font = pygame.font.SysFont(None, 30)
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    game_display.blit(score_text, [10, 10])
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += 5
    object_y += object_speed

    if object_y > height:
        object_y = 0
        object_x = random.randint(0, width - object_size)
    if (
        player_x < object_x < player_x + player_size
        or player_x < object_x + object_size < player_x + player_size
    ) and (
        player_y < object_y < player_y + player_size
        or player_y < object_y + object_size < player_y + player_size
    ):
        score += 1
        object_y = 0
        
        
        randR = random.randint(0, 255)
        if randR > 122.5:
            randR=255
        elif randR < 122.5:
            randR=0 

        if randR == 0:
            randG=random.randint(0, 255)
        if randG > 122.5:
            randG=255
        elif randG < 122.5:
            randG=0 
        else:
            randG=0
        if randG==0:
            randB=random.randint(0, 255)
        if randB > 122.5:
            randB=255
        elif randB < 122.5:
            randB=0 
    R = randR
    G = randG
    B = randB
    object_color = (R, G, B)
        
        
        
    #object_x = random.randint(0, width - object_size)




    game_display.fill(black)
    pygame.draw.rect(game_display, player_color, [player_x, player_y, player_size, player_size])
    pygame.draw.rect(game_display, object_color, [object_x, object_y, object_size, object_size])
    display_score(score)
    pygame.display.update()

    clock.tick(60)

# Quit the game
pygame.quit()
quit()
