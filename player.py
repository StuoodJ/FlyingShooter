
def Player(screen, playercolor, playerrect, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerx -= 350 * dt
    if keys[pygame.K_RIGHT]:
        playerx += 350 * dt
    if keys[pygame.K_UP]:
        playery -= 650 * dt
    if keys[pygame.K_DOWN]:
        playery += 650 * dt
    pygame.draw.rect(screen, playercolor, playerrect)
    