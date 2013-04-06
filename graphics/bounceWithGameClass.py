import pygame
import random
import math
import os

class Game(object):
    def __init__(self): #initializer, sets up pygame, window and tools
        pygame.init()
        self.screenHeight=600
        self.screenWidth=600
        self.blue=(0,0,255)
        self.red=(255,0,0)
        self.black=(0,0,0)
        self.clock=pygame.time.Clock() #clock for ticking
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        self.screen=pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.background=pygame.Surface((self.screenWidth, self.screenHeight))
        #self.screen.fill(self.blue)
        self.background.fill(self.black)
        self.screen.blit(self.background, (0,0))
        pygame.display.flip() # what is the difference between blit and flip?
        self.movingsprites=pygame.sprite.RenderUpdates() # sprite list
        # create ball
        self.ball=Ball((self.screenWidth/2,self.screenHeight/2))
        self.movingsprites.add(self.ball)

        
    def run(self):
        running = True
        while running:
            self.clock.tick(30) # tick pygame clock.  Limit the fps by passing desired frames/sec
            running=self.handleEvents()
            self.manageBall()
            for sprite in self.movingsprites:
                sprite.update()
            self.movingsprites.clear(self.screen, self.background)
            dirty=self.movingsprites.draw(self.screen)
            #self.movingsprites.update()
            pygame.display.update(dirty)
        print("Quitting. Thanks for playing.")
           
    def handleEvents(self):
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return False
           elif event.type == pygame.KEYDOWN:
               print("keydown")
               if event.key == pygame.K_SPACE:
                   if self.ball.velx == 0 and self.ball.vely == 0:
                       print("space")
                       self.ball.serve()
               if event.key == pygame.K_n:
                   self.ball.serve()
               if event.key == pygame.K_ESCAPE:
                   return False
                   
        return True
    def manageBall(self):
        # runs the game by moving the ball and handling positions
        # move ball according to its velocity        
        self.ball.rect.x += self.ball.velx
        self.ball.rect.y += self.ball.vely
        #print("manageBall:x,y",self.ball.rect.x, self.ball.rect.y)
        # check if ball is off the top
        if self.ball.rect.top <0:
            self.ball.rect.top=0
            self.ball.vely *= -1
        
        elif self.ball.rect.left <= 0:
            self.ball.rect.left = 0
            self.ball.velx *= -1
        
        elif self.ball.rect.right > self.screenWidth:
            self.ball.rect.right = self.screenWidth
            self.ball.velx *= -1
        
        elif self.ball.rect.bottom > self.screenHeight:
            self.ball.rect.bottom = self.screenHeight
            self.ball.vely *= -1

        # give a little of the paddle's velocity to the ball
        self.ball.vely += hitpaddle.velocity/3.0



class Ball(pygame.sprite.Sprite):
    def __init__(self, xy):
    	print("Ball::init")
        pygame.sprite.Sprite.__init__(self)
        self.white=(255,255,255)
        self.red=(255,0,0)
        self.image = pygame.Surface([15,15])
        self.image=pygame.image.load(os.path.join('icon9.png'))
        self.image.set_colorkey(self.white)
        
        #self.image.fill(self.red)
        self.rect=self.image.get_rect()
        
        self.rect.centerx, self.rect.centery = xy
        self.maxpeed = 10
        self.servespeed = 5
        self.velx = 0
        self.vely = 0
        print("centerx,centery",self.rect.centerx,self.rect.centery)
        
    def reset(self):
        self.rect.centerx, self.rect.centery=200,200
        self.velx=0
        self.vely=0
              
    def serve(self):
        angle=random.randint(-90,90)
        print("angle=", angle)
        x=math.cos(math.radians(angle))
        y=math.sin(math.radians(angle))
        
        self.velx=self.servespeed * x
        self.vely=self.servespeed*y
        print("x,y", self.velx, self.vely)

if __name__=='__main__':	# what does this mean?
	game=Game()
	game.run()
                
    	    