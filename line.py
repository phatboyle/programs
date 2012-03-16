import pygame

x=0
y=0
n=4
screenWidth=400
screenHeight=400
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
test=(255,20,147)
black=(0,0,0)
pink=(255,20,147)

screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(black)

pygame.draw.line(screen, blue, (300, 50), (20, 300))


#while x <= screenWidth: 
#    pygame.draw.line(screen, blue, (screenWidth-x, 0), (0, y))
#    pygame.draw.line(screen, red, (0, y), (0+x, screenHeight))
#    pygame.draw.line(screen, test, (0+x, screenHeight), (screenWidth, screenHeight-y))
#    pygame.draw.line(screen, white, (screenWidth, screenHeight-y), (screenWidth-x, 0))      
#    x=x+n
#    y=y+n
	#    print("x,y",400-x,0,0,y
pygame.display.flip() 

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break;
