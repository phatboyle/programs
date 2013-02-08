# Listing_18-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# add a score
# player gets 3 paddles and can earn more with a higher score
# sound
# if the paddle is moving when it hits the ball, then the ball will bounce accordingly
# perplexus
# multicolor bricks

import pygame, sys
import random
# defines a class
class MyBallClass(pygame.sprite.Sprite):
    # defines what the class will do
   def __init__(self, image_file, speed, location):                      
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer     
        self.image = pygame.image.load(image_file)                       
        self.rect = self.image.get_rect()                                
        self.rect.left, self.rect.top = location                         
        self.speed = speed                                               
    # defines a method inside a class
    
   def move(self):                                                       
        if self.rect.left <= screen.get_rect().left or  self.rect.right >= screen.get_rect().right:             
            self.speed[0] = - self.speed[0]
        if self.rect.top <= screen.get_rect().top:
            self.speed[1] = -self.speed[1]          
        newpos = self.rect.move(self.speed)                              
        self.rect = newpos                                               

# defines a class
class MyPaddleClass(pygame.sprite.Sprite):
    # defines what the class will do
    def __init__(self, location):                                        
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer        
        image_surface = pygame.surface.Surface([100, 20])                
        image_surface.fill([0,0,0])                                      
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()                           
        self.rect.left, self.rect.top = location 
# defines a class
class MyBrickClass(pygame.sprite.Sprite):
    # defines what the class will do
    def __init__(self, location, size):                                        
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer        
        image_surface = pygame.surface.Surface([size[0], size[1]])                
        image_surface.fill([178,34,34])                                      
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()                           
        self.rect.left, self.rect.top = location 

# defines a method inside the class
    def remove(self):
        self.rect.left, self.rect.top = [-100,-100]
# start
pygame.init()                                                            
# makes a screen
brickWidth = 75
brickHeight = 20
brickSize = [brickWidth, brickHeight]

screen = pygame.display.set_mode([640,480])                              
background = pygame.Surface(screen.get_size())                           
background.fill([255, 255, 255])                                         
clock = pygame.time.Clock()
# gets bouncing ball
a = random.randint(20,640)
b = random.randint(1,420)
myBall = MyBallClass('wackyball.bmp', [5,5], [a,b])

#  makes the paddle
paddle = MyPaddleClass([270,400])  
paddleGroup = pygame.sprite.Group(paddle)
# makes the bricks
x = 105
y = 50
brick_list = []
for i in range(1,6):
    brick = MyBrickClass([x,y], brickSize)
    brick_list.append(brick)
    x = x + brickWidth  + 2
x = 105
y = y + 20
for j in range(1,6):
    brick = MyBrickClass([x,y], brickSize)
    brick_list.append(brick)
    x = x + brickWidth + 2
lives = 3
brickGroup = pygame.sprite.Group(brick_list)
points = 0
bricks = 10
n = 0
m = 0
c = 0

while True:
    # says how fast the loop will run(in milliseconds)
    clock.tick(36)
    screen.fill([255,255,255])
    
    font = pygame.font.Font(None,50)
    string_render = font.render(str(points),1,(0,0,0))
    pPos = [10,10]
    screen.blit(string_render,pPos)
    #display the amount left
    for k in range(lives):
        width = screen.get_rect() .width
        screen.blit(myBall.image,[width - 40 * k,20])
    # if the red x is clicked close the window
    for event in pygame.event.get():                                     
        if event.type == pygame.QUIT:                                    
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    
    if pygame.sprite.spritecollide(myBall,paddleGroup, False):
        myBall.speed[1] = -myBall.speed[1]
 
    e = pygame.sprite.spritecollide(myBall,brickGroup,True)
    if e <> []:
        myBall.speed[1] =- myBall.speed[1]
        brick.remove
        points = points + 1
        bricks = bricks - 1
        
    if myBall.rect.top >= screen.get_rect() .bottom:
        lives = lives - 1
        pygame.time.delay(2000)
        myBall.rect.topleft = [50,50]
        c = 1

    if bricks == 5:
        x = 105
        y = y + 20
        if n == 5:
            y = y - 120
            n = n - 5
        brick_list2 = []
        for i in range(1,6):
            brick = MyBrickClass([x,y],brickSize)
            brick_list2.append(brick)
            x = x + brickWidth + 2
        brickGroup.add(brick_list2)
        n = n + 1
        bricks = bricks + 5

    if m == 10:
        if c == 0:
            lives = lives + 1
            m = 0
            c = 0
        if c == 1:
            m = 0
            c == 0
    # move the ball
    myBall.move()
    screen.blit(myBall.image,myBall.rect)

    screen.blit(paddle.image, paddle.rect)
    brickGroup.draw(screen)
    # put everything on real screen
    pygame.display.flip()
    