import pygame, os, sys
from pygame.locals import *
from random import randint


class Enemy(pygame.sprite.Sprite):
        ''' A simple sprite that bounces off the walls '''
        
        def load_image(self, image_name):
                ''' The proper way to load an image '''
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        print "Cannot load image: " + image_name
                        raise SystemExit, message
                return image.convert_alpha()

        def __init__(self, screen, init_x, init_y, init_x_speed, init_y_speed):
                ''' Create the Enemy at (x, y) moving up at a given speed '''
                pygame.sprite.Sprite.__init__(self) #call Sprite intializer
                
                # Load the image
                self.image = self.load_image('assets/comp11-1.png')

                # Create a moving collision box
                self.rect = self.image.get_rect()
                self.rect.x = init_x
                self.rect.y = init_y
                self.rect.move(self.rect.x, self.rect.y)
                self.screen = screen 
                
                # Set the (x, y)
                self.x = init_x
                self.y = init_y

                #get dimensions                
                self.image_w, self.image_h = self.image.get_size()
                
                # Set the default speed (dx, dy)
                self.dy = init_y_speed
                self.dx = init_x_speed

                self.active = True
                                
        def update(self):
                ''' Move the Enemy '''
                if ((self.x + self.dx) <= 5):
                        self.dx = self.dx * -1
                if ((self.x + self.dx) >= self.screen.get_size()[0]):
                        self.dx = self.dx * -1
                if ((self.y + self.dy) <= 5):
                        self.dy = self.dy * -1
                if ((self.y + self.dy) >= self.screen.get_size()[1]):
                        self.dy = self.dy * -1
                self.x += self.dx
                self.y += self.dy
                self.rect.y += self.dy
                self.rect.x += self.dx
                self.rect.move(self.rect.x, self.rect.y)


        def is_shot(self):
                '''actions if muta is shot by laser'''
                self.active = False
                draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
                self.image = self.load_image('assets/laser_explosion.gif')
                self.screen.blit(self.image, draw_pos)
                self.kill()


        def draw(self):
                ''' Draw the Enemy on the screen '''
                draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
                self.screen.blit(self.image, draw_pos)                              



if __name__ == "__main__":
        # Check if sound and font are supported
        if not pygame.font:
                print "Warning, fonts disabled"
        if not pygame.mixer:
                print "Warning, sound disabled"
                
        # Constants
        FPS = 50
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
        BACKGROUND_COLOR = (255, 255, 255)
        
        # Initialize Pygame, the clock (for FPS), and a simple counter
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        clock = pygame.time.Clock()

        # Create the sprite group
        muta = pygame.sprite.Group()

        for i in xrange(0,10):
                muta.add(Enemy(screen, randint(1, SCREEN_WIDTH), 50, randint(1, 10), randint(1, 10)))

        # Game loop
        while True:
                time_passed = clock.tick(FPS)
                # Event handling here (to quit)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()                                      
                
                # Redraw the background
                screen.fill(BACKGROUND_COLOR)
                
                # Update and redraw all sprites
                muta.update()
                muta.draw(screen)
                
                # Draw the sprites
                pygame.display.update()

