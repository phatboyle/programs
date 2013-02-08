# Listing_17-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Using sprites to put multiple ball images on the screen

import sys, pygame

#-----ball subclass definition -----------------------------
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
 		self.speed = speed
 	def move(self):
 	    self.rect = self.rect.move(self.speed)
 	    if self.rect.left < 0 or self.rect.right > width:
 	        self.speed[0] = -self.speed[0]
 	        
 	    if self.rect.top < 0 or self.rect.bottom > hight:
 	        self.speed[1] = -self.speed[1]    
#----- Main Program -----------------------------
size = width, height = 640, 480                          
screen = pygame.display.set_mode(size)                   
screen.fill([255, 255, 255])                             
img_file = "beach_ball.png"
balls = []
for row in range (0, 3):
    for column in range (0, 3):
        location = [column * 180 + 10, row * 180 + 10]
        ball = MyBallClass(img_file, location)
        balls.append(ball)  # Collect the balls in a list
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()