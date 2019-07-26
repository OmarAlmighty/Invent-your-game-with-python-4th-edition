import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 500
WINDOWHIEGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# Set up the colors.
WHITE = (255, 255, 255)

# Set up the block data structure.
player = pygame.Rect(300, 100, 40, 40)
playerImg = pygame.image.load('player.png')
playerStrechedImg = pygame.transform.scale(playerImg, (40, 40))
foodImg = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHIEGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

# Set up the music.
pickUpSound = pygame.mixer.Sound('pickUp,wav')
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_x:
                player.top = random.randint(0, (WINDOWHIEGHT - player.height))
                player.left = random.randint(0, (WINDOWWIDTH - player.width))
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHIEGHT - 20), 20, 20))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and player.bottom < WINDOWHIEGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the block onto the surface.
    windowSurface.blit(playerStrechedImg, player)

    # Check whether the block has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStrechedImg = pygame.transform.scale(playerImg, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()

    # Draw the food.
    for food in foods:
        windowSurface.blit(foodImg, food)

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)
