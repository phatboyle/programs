import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x = 50 
y = 50
x_speed = 5
#screen.blit(my_ball, [x,y])
#pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
    pygame.time.delay(20)
    # screen.blit(my_ball, [150,50])
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + x_speed
    if x > screen.get_width():
        x = 0
    #x = x + 5
    screen.blit(my_ball, [x,y])
    pygame.display.flip()
    