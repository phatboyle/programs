import pygame

class Game(object):
    def __init__(self): #initializer, sets up pygame, window and tools
        pygame.init()
        screenHeight=400
        screenWidth=400
        blue=(0,0,255)
        self.clock=pygame.time.Clock() #clock for ticking
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
        # create ball
        self.ball=Ball((200,200))
        self.movingsprites.add(self.ball)
        

        self.screen=pygame.display.set_mode((screenHeight, screenWidth))
        #self.background=pygame.Surface((screenHeight, screenWidth))
        self.screen.fill(blue)
        #self.background.fill(blue)
        #self.screen.blit(self.background, (0,0))
        #pygame.display.flip() # what is the difference between blit and flip?
        self.movingsprites=pygame.sprite.RenderPlain() # sprite list
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60) # tick pygame clock.  Limit the fps by passing desired frames/sec
            running=self.handleEvents()
            self.manageBall()
            self.movingsprites.update()
            screen.fill(blue)
            self.movingsprites.draw(screen)
            pygame.display.flip()
            print("Quitting. Thanks for playing.")
           
    def handleEvents(self):
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return False
           elif event.type == pygame.KEYDOWN:
               if event.key == K_ESCAPE:
                   return False
               if event.key == K_w:
                   
               
                return True


class Ball(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join('icon1.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = xy
        self.maxpeed = 10
        self.servespeed = 5
        self.velx = 0
        self.vely = 0
        
    def reset(self):
        self.rect.centerx, self.rect.centery=200,200
        self.velx=0
        self.vely=0
    
    def serve(self):
        angle=random.randint(-45,45)
        x=math.cos(math.radians(angle))
        y=math.sin(math.radians(angle))
        
        self.velx=self.servespeed * x
        self.vely=self.servespeed*y
    

        
if __name__=='__main__':	# what does this mean?
	game=Game()
	game.run()
                
    	    
    
    
    
