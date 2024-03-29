# Jessie Chapman
# Laser.py - Module for a single laser if used with Battlecruiser.py,
#            or shows a stream of laser when run alone.
# Date: 2/22/2014

import pygame, os, sys
from pygame.locals import *
from random import randint

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
X_POS = 550
X_SPEED = 8
Y_SPEED = -8
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

class Laser(pygame.sprite.Sprite):

    def load_image(self, img):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(img)
        except pygame.error, message:
            print "Cannot load image: " + img
            raise SystemExit, message
        return image.convert_alpha()


    def __init__(self, x, y, x_speed, y_speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = self.load_image("laser.gif")
        self.x = x
        self.y = y
        self.dx = x_speed
        self.dy = y_speed
        self.active = True

        # Make a bounding box from the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_width, self.image_height = self.image.get_size()

    def draw(self, screen):
        self.screen = screen
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        ''' Move the sprite '''
        self.y += self.dy
        self.rect.y += self.dy
        self.rect.move(self.rect.x, self.rect.y)
            
        # Remove sprite from group if it goes off the screen...
        if self.rect.y <= 0:
            self.kill()

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
    screen = pygame.display.set_mode(screenDims, 0, 32)
    pygame.display.set_caption('Laser.py')

    lasers = pygame.sprite.Group()
    clock = pygame.time.Clock()

    while True:
        time_passed = clock.tick(FPS)
        lasers.add(Laser(randint(1, SCREEN_WIDTH), X_POS, X_SPEED, Y_SPEED))
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BACKGROUND_COLOR)
        lasers.update()
        lasers.draw(screen)
        pygame.display.update()
