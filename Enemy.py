# Jessie Chapman
# Enemy.py - Displays 10 enemies, bouncing off the sides of the screen
# Date: 3/4/2014

import pygame, os, sys
from pygame.locals import *
from random import randint

##################################################
# Enemy sprite                                   #
##################################################

class Enemy(pygame.sprite.Sprite):
    '''The Enemy sprite'''

    def load_image(self, img):
        '''Try to load the sprite's image; exit otherwise'''
        try:
            image = pygame.image.load(img)
        except pygame.error, message:
            print "Cannot load image: " + image
            raise SystemExit, messge
        return image.convert_alpha()

    def __init__(self, screen, x, y, x_speed, y_speed):
        '''Initial conditions for the Battlecruiser'''
        pygame.sprite.Sprite.__init__(self)

        self.image = self.load_image("mutalisk.gif")
        self.explosion = self.load_image("laser_explosion.gif")
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = x_speed
        self.dy = y_speed
        self.active = True
        self.exploded = False

        # Make a bounding box from the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_width, self.image_height = self.image.get_size()

        # Put bounding box in the same place as the sprite
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_width, self.y + self.image_height)

    def update(self):
        '''Update the sprite's position on the screen'''
        if self.active == True:
            if ((self.x + self.dx) <= 0):
                self.dx = self.dx * -1
            if ((self.x + self.dx) >= self.screen.get_size()[0]):
                self.dx = self.dx * -1
            if ((self.y + self.dy) <= 0):
                self.dy = self.dy * -1
            if ((self.y + self.dy) >= self.screen.get_size()[1]):
                self.dy = self.dy * -1
            self.x = self.x + self.dx
            self.y = self.y + self.dy
        
            #self.rect.x = self.x + self.dx
            #self.rect.y = self.y + self.dy
            self.rect.move(self.x, self.y)
            self.rect.topleft = (self.x, self.y)
            self.rect.bottomright = (self.x + self.image_width, self.y + self.image_height)

    def draw(self):
        '''Method to put the sprite on the screen'''
        if self.active == True:
            self.draw_pos = self.image.get_rect().move(self.x - self.image_width/2, self.y - self.image_height/2)
            self.screen.blit(self.image, self.draw_pos)
        elif self.exploded == True and self.active == False:
            self.draw_pos = self.image.get_rect().move(self.x - self.image_width/2, self.y - self.image_height/2)
            self.screen.blit(self.explosion, self.draw_pos)
            self.exploded = False

    def explode(self):
        self.exploded = True

    def deactivate(self):
        self.active = False

if __name__ == "__main__":            

    #constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    FPS = 50
    MAX_SPEED = 10
    BACKGROUND_COLOR = (255, 255, 255)
    NUM_SPRITES = 10
    COUNTER_LOCATION = (10, 10)

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
    pygame.display.set_caption('Enemy.py')

    # Prep screen for images
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    bground_img = pygame.image.load("ram_aras.png")
    screen.blit(bground_img, (0,0))
    pygame.display.flip()

    # Set up timer/clock; 50 frames per second
    clock = pygame.time.Clock()
    #pygame.time.set_timer(USEREVENT + 1, 1000)

    sprites = []
    for i in range(NUM_SPRITES):
        sprites.append(Enemy(screen, randint(1, SCREEN_WIDTH), randint(1, SCREEN_HEIGHT), randint(1, MAX_SPEED), randint(1, MAX_SPEED)))

#######################################
# Game Loop                           #
#######################################

    while True:
        time_passed = clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_ESCAPE:
                    quit()

        screen.fill(BACKGROUND_COLOR)

        for sprite in sprites:
            sprite.update()
            sprite.draw()
        
        pygame.display.flip()
