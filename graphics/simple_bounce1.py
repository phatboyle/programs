import pygame
import random
import sys, os, math 
 
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
 
 
# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill((blue))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        
# This class represents the bar at the bottom that the player controls
class Ball(pygame.sprite.Sprite):
 
    # Set speed vector
    change_x=0
    change_y=0
    walls=None
    paddles=None
    iconimg=None
     
    # Constructor function
    def __init__(self,x,y,walls, paddles):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
  
        # Set height, width
        self.image = pygame.Surface([15, 15])
        #self.image.fill(white)
        self.image=pygame.image.load(os.path.join('icon1.png'))
        self.image.set_colorkey(white)
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
         
        self.walls=walls
        self.paddles=paddles
        print "created ball"
        print self.paddles
         
    # Find a new position for the player
    def update(self):
        # Get the old position, in case we need to go back to it
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x
         
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, self.walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x
            self.change_x *= -1
        
        collide1 = pygame.sprite.spritecollide(self, self.paddles, False)
        if collide1:
            print ("paddle collided")
 
        old_y=self.rect.top
        new_y=old_y+self.change_y
        self.rect.top = new_y
         
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, self.walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.top=old_y
            self.change_y *= -1
             
        if self.rect.x < -20 or self.rect.x > screen_width + 20:
            self.change_x = 0
            self.change_y = 0
 
             
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 600x600 sized screen
screen_width = 600
screen_height = 600
 
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Set the title of the window
pygame.display.set_caption('Pong')
 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Used for converting color maps and such
background = background.convert()
 
# Fill the screen with a black background
background.fill(black)
 
# All sprite lists
wall_list=pygame.sprite.RenderPlain()
all_sprites=pygame.sprite.RenderPlain()
movingsprites = pygame.sprite.RenderPlain()
paddlesprites = pygame.sprite.RenderPlain()
 
# Create the players
player1 = Player(10,screen_height/2)
all_sprites.add(player1)
wall_list.add(player1)
movingsprites.add(player1)
paddlesprites.add(player1)
 
# Make the walls. (x_pos, y_pos, width, height)
# Top wall
wall=Wall(0,0,screen_width,10) 
wall_list.add(wall)
all_sprites.add(wall)
 
# Bottom wall
wall=Wall(0,screen_height-10,screen_width,screen_height) 
wall_list.add(wall)
all_sprites.add(wall)

# Right wall
wall=Wall(screen_width-10,0,screen_width,screen_height) 
wall_list.add(wall)
all_sprites.add(wall)

# Font
score=Score(screen_width/2,30)
all_sprites.add(score)
 
# Create the ball
ball = Ball( -50,-50, wall_list, paddlesprites )
movingsprites.add(ball)
all_sprites.add(ball)
 
clock = pygame.time.Clock()
 
done = False
 
# Main program loop
while done == False:
     
    # Loop through any window events
    for event in pygame.event.get():
        # The user clicked 'close' or hit Alt-F4
        if event.type == pygame.QUIT:
            done=True
             
        # The user clicked the mouse button
        # or pressed a key
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
             
            # Is the ball not moving?
            if ball.change_y == 0:
                 
                # Start in the middle of the screen at a random y location
                ball.rect.x = screen_width/2
                ball.rect.y = random.randrange(10,screen_height-20)
                 
                # Set a random vector
                ball.change_y = random.randrange(-5,6)
                ball.change_x =  random.randrange(5,10)
                 
                # Is the ball headed left or right? Select randomly
                if( random.randrange(2) == 0 ):
                    ball.change_x *= -1
 
    # Update the ball position. Pass it the list of stuff it can bounce off of
    movingsprites.update()
     
    # Clear the screen
    screen.fill(black)
     
    # Draw the sprites
    all_sprites.draw(screen)
 
    # Display the screen
    pygame.display.flip()
 
    clock.tick(30)
 
# All done, shut down Pygame            
pygame.quit()