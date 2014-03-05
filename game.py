# Jessie Chapman
# game.py - A playable Battle for Ram Aras with 4 enemies
# Date: 3/4/2014

import pygame, os, sys
from pygame.locals import *
from random import randint

# Import the modules
from Battlecruiser import *
from Laser import *
from Enemy import *

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 50
MAX_SPEED = 6
BACKGROUND_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (0, 0, 0)
NUM_SPRITES = 4

if __name__ == "__main__":

    # Check if sound and font are supported
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"

    # How to exit
    def quit():
        '''Quits the game'''
        pygame.quit()
        sys.exit(0)

    # Initialize the pygame modules to prep for the game
    pygame.init()

############################################
# Setting up the screen, sprites           #
############################################

    # Set up the screen, window dimensions
    screenDims = (SCREEN_WIDTH, SCREEN_HEIGHT)
    window = pygame.display.set_mode(screenDims, pygame.RESIZABLE)
    pygame.display.set_caption('Battlecruiser.py')

    # Prep screen for images
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    bground_img = pygame.image.load("ram_aras.png")
    screen.blit(bground_img, (0,0))
    pygame.display.flip()

    # Set up timer/clock; 50 frames per second
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT + 1, 1000)

    # Variable to keep track of the key pressed
    pressed = None

    # Keep track of score
    score = 0

    # Font:
    font = pygame.font.Font(None, 36)

    # The sprite, at position (10, 10)
    battlecruiser = Battlecruiser(screen, 10, 10, 5, 5)
    enemies = []
    for i in range(NUM_SPRITES):
        enemies.append(Enemy(screen, randint(1, SCREEN_WIDTH), randint(1, SCREEN_HEIGHT), 4, 4))

    game_over = False

#######################################
# Game Loop                           #
#######################################

    while game_over == False:
        time_passed = clock.tick(FPS)

        # Check for collisions
        for enemy in enemies:
            for laser in battlecruiser.lasers:
                if pygame.sprite.collide_rect(laser, enemy) and enemy.active == True:
                    enemy.explode()
                    enemy.deactivate()
                    score = score + 100
            if pygame.sprite.collide_rect(battlecruiser, enemy) and enemy.active == True:
                battlecruiser.explode()
                enemy.deactivate()
                game_over = True

        # Update and draw battlecruiser, lasers, enemies
        battlecruiser.update(pressed)
        battlecruiser.lasers.update()
        battlecruiser.draw(bground_img)
        battlecruiser.lasers.draw(window)
        for enemy in enemies:
            enemy.update()
            enemy.draw()
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_ESCAPE:
                    quit()
                elif event.key == K_UP:
                    pressed = "UP"
                elif event.key == K_DOWN:
                    pressed = "DOWN"
                elif event.key == K_LEFT:
                    pressed = "LEFT"
                elif event.key == K_RIGHT:
                    pressed = "RIGHT"
                elif event.key == K_SPACE:
                    battlecruiser.fire()
                else:
                    pressed = None

        # Render the score to the screen
        score_display = font.render("Score: " + str(score), 1, BACKGROUND_COLOR)
        screen.blit(score_display, (10, 10))

        pygame.display.flip()

#######################################
# End of Game Loop                    #
#######################################

    while game_over == True:
        screen.fill(GAME_OVER_COLOR)
        game_over_display = font.render("Game Over", 1, BACKGROUND_COLOR)
        screen.blit(game_over_display, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_ESCAPE:
                    quit()
