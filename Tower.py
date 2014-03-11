# Jessie Chapman, Todd Pollak, Jared Bronen, Sam Sprague
# Tower.py

import pygame, os, sys
from pygame.locals import *
from random import randint

##################################################
# Tower sprite                                   #
##################################################

class Tower(pygame.sprite.Sprite):
    '''The Tower sprite'''

    def load_image(self, img):
        '''Try to load the sprite's image; exit otherwise'''
        try:
            image = pygame.image.load(img)
        except pygame.error, message:
            print "Cannot load image: " + image
            raise SystemExit, messge
        return image.convert_alpha()

    def __init__(self, screen, pos):
        '''Initial conditions for the Tower'''
        pygame.sprite.Sprite.__init__(self)

        self.image = self.load_image("TOWER SPRITE FILE")
        self.screen = screen
        self.pos = pos #passed in from pygame.mouse.get_pos() if event.type == MOUSEBUTTONDOWN
        self.x, self.y = self.pos

        # Make initial bounding box from the sprite
        self.rect = self.image.get_rect()
        self.rect.pos = self.pos
        self.rect.x, self.rect.y = self.pos
        self.image_w, self.image_h = self.image.get_size()
        self.rect.w = self.image_w
        self.rect.h = self.image_h

        # Need a "radius" for the Tower: 
        # increase the bounding box 1.5 times its orig size
        self.rect.w = self.image_w * 1.5
        self.rect.h = self.image_h * 1.5

        # Fix self.rect.x and self.rect.y to correspond 
        # to new bounding box's top left x, y:
        self.rect.x = self.y - ( (self.rect.h - self.image_h) / 2)
        self.rect.x = self.x - ( (self.rect.w - self.image_w) / 2)

        # Update the (x, y) position vars for both box and sprite:
        self.rect.pos = self.rect.x, self.rect.y
        self.pos = self.rect.pos
        self.x, self.y = self.pos

        # Put bounding box in the same place as the sprite
        self.rect.move(self.x, self.y)

    def update(self):
        # Cooldown


    def draw(self):
        '''Method to draw Tower sprite at the mouse position'''
        self.draw_pos = self.image.get_rect().move(self.x - self.image_w/2, self.y - self.image_h/2)
        self.screen.blit(self.image, self.draw_pos)


# leftover from Enemy.py, delete when finished:
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
