# Jessie Chapman
# Battlecruiser.py - Move the battlecruiser around the screen
#                    and shoot lasers with the space bar
# Date: 2/22/2014

import pygame, os, sys, random
from Laser import *
from pygame.locals import *

##################################################
# Battlecruiser sprite                           #
##################################################

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
FPS = 50

class Battlecruiser(pygame.sprite.Sprite):
    '''The Battlecruiser sprite'''

    def load_image(self, img):
        '''Try to load the sprite's image; exit otherwise'''
        try:
            image = pygame.image.load(img)
        except pygame.error, message:
            print "Cannot load image: " + image
            raise SystemExit, messge
        return image.convert_alpha()

    def load_sound(self, sound_name):
        try:
            sound = pygame.mixer.Sound(sound_name)
        except pygame.error, message:
            print "Cannot load sound: " + sound_name
            raise SystemExit, message
        return sound

    def __init__(self, screen, x, y, x_speed, y_speed):
        '''Initial conditions for the Battlecruiser'''
        pygame.sprite.Sprite.__init__(self)

        self.image = self.load_image("battlecruiser.gif")
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = x_speed
        self.dy = y_speed
        self.active = True
        self.lasers = pygame.sprite.Group()

        # Make a bounding box from the sprite
        self.rect = self.image.get_rect()
        self.image_width, self.image_height = self.image.get_size()

        # Put bounding box in the same place as the sprite
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_width, self.y + self.image_height)
        
    def draw(self, bground_img):
        '''Method to put the sprite on the screen'''
        self.screen.blit(bground_img, (0,0)) 
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        self.lasers.add(Laser(self.x + self.image_width/2, self.y, 0, -6))
        fired_sound = self.load_sound("laser.wav")
        fired_sound.play()

    def explode(self):
        death_sound = self.load_sound("death_explode.wav")
        death_sound.play()
        self.active = False

    def update(self, direc):
        '''Update the sprite's position on the screen based'''
        '''on user's key presses; bound it within the screen'''
        '''Update sprite first, then bounding box follows'''
        if direc == "UP":
            self.y = self.y - 3
            if self.y < 0:
                self.y = 0
        elif direc == "DOWN":
            self.y = self.y + 3
            if self.y > SCREEN_HEIGHT - self.image_height:
                self.y = SCREEN_HEIGHT - self.image_height
        elif direc == "LEFT":
            self.x = self.x - 3
            if self.x < 0:
                self.x = 0
        elif direc == "RIGHT":
            self.x = self.x + 3
            if self.x > SCREEN_WIDTH - self.image_width:
                self.x = SCREEN_WIDTH - self.image_width

        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_width, self.y + self.image_height)

if __name__ == "__main__":            

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
    seconds = 0
    pygame.time.set_timer(USEREVENT + 1, 1000)

    # Variable to keep track of the key pressed
    pressed = None

    # The sprite, at position (10, 10)
    battlecruiser = Battlecruiser(screen, 10, 10, 5, 5)

#######################################
# Game Loop                           #
#######################################

    while True:
        clock.tick(FPS)
        battlecruiser.update(pressed)
        battlecruiser.lasers.update()
        battlecruiser.draw()
        battlecruiser.lasers.draw(window)
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
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
