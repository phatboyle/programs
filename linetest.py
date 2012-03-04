import pygame

screenHeight=400
screenWidth=400
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
pink=(255,51,255)

screen=pygame.display.set_mode((screenWidth, screenHeight))
pygame.draw.line(screen,red , (0, 0), (screenWidth, screenHeight))

x=0
y=0
inc=1
r=pygame.Rect(x,y,50,50)

while True:
	screen.fill(pink)
	r=r.move(inc,inc)
	pygame.draw.rect(screen,blue,r)
	pygame.display.flip() # draw it 
	if x>350:
	    inc=inc*-1
	if x<0:
	    inc=inc*-1
	event=pygame.event.poll()
	if event.type == pygame.QUIT:
	    break
	elif event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_ESCAPE:
	        break
