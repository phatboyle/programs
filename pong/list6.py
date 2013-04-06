# Listing_18-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# make the brick creation a function
# figure out why the ball bounces in and out of the paddle and how to keep it from doing it
# make it start in a random direction going down


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
        image_surface = pygame.surface.Surface([100, 8])                
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
a = random.randint(1,640)
b = random.randint(100,150)
myBall = MyBallClass('wackyball.bmp', [1,1], [a,b]) # initializes the ball

#  makes the paddle
paddle = MyPaddleClass([270,400])  
paddleGroup = pygame.sprite.Group(paddle)
# makes the bricks
brick_list = []

# updated by Pat
x = 40
y = 50
for i in range (1,4):
    for j in range(1,8):
        brick = MyBrickClass([x,y], brickSize)
        brick_list.append(brick)
        x = x + brickWidth + 5
        screen.blit(brick.image, [x,y]) # blit each brick as you make them
    brickGroup = pygame.sprite.Group(brick_list) 
    y = y + brickHeight+5
    x=40
pygame.display.flip()   # flip
    
lives = 3

points = 0
n = 0
m = 0
c = 0
paddleVelocity=0
paddlePos1=0
paddlePos2=0

while True:
    # says how fast the loop will run(in milliseconds)
    clock.tick(60)
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
    
    events = pygame.event.get()
    if events != []:
        for event in events:                                     
            if event.type == pygame.QUIT:                                    
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                paddle.rect.centerx = event.pos[0]
                paddlePos2=paddle.rect.centerx
                paddleVelocity = paddlePos2-paddlePos1
                paddlePos1=paddlePos2
    else:
        paddleVelocity=0
    #print paddlePos1, paddlePos2, paddleVelocity   

    if pygame.sprite.spritecollide(myBall,paddleGroup, False):  # paddle collision and physics for ball
        myBall.speed[1] = -myBall.speed[1]
        myBall.speed[0]= myBall.speed[0]+paddleVelocity/5
        

      #  myBall.speed[0]= 5 #x
       # myBall.speed[1]=5 #y

    if len(brickGroup.sprites()) <= 0:
            brickGroup = bricker(brick_list)

    e = pygame.sprite.spritecollide(myBall,brickGroup,True)
    if e <> []:
        myBall.speed[1] =- myBall.speed[1]
        brick.remove
        points = points + 1
        m = m + 1
    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        pygame.time.delay(2000)
        myBall.rect.topleft = [50,50]
        c = 1 # if c==1, then ball has gone off the screen 

    if m == 10:     # m is the score
        m=0
        lives = lives + 1
    if lives == 0:
        sys.exit()  # TODO:  maybe you should print a message?
    if myBall.speed[1]>=100:
        myBall.speed = 20
    # move the ball
    myBall.move()
    screen.blit(myBall.image,myBall.rect)

    screen.blit(paddle.image, paddle.rect)
    brickGroup.draw(screen)
    # put everything on real screen
    pygame.display.flip()    