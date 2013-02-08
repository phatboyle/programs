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
]
# start
pygame.init()                                                            
# makes a screen

screen = pygame.display.set_mode([640,480])                              
background = pygame.Surface(screen.get_size())                           
background.fill([255, 255, 255])                                         

#  makes the paddle


font = pygame.font.Font(None,50)
string_render = font.render("Pong",1,(0,255,255))
pPos = [40,100]
screen.blit(string_render,pPos)
pygame.display.flip()


screen.fill([255,255,255])
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
    
#    if pygame.sprite.spritecollide(brick,ballGroup, False):
#        myBall.speed[1] = -myBall.speed[1]
#        brick.remove()
        
    # move the ball
    myBall.move()
    screen.blit(myBall.image,myBall.rect)

    screen.blit(paddle.image, paddle.rect)
    brickGroup.draw(screen)
    # put everything on real screen
    pygame.display.flip()
    