import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([400,400])
red = [255,0,0]
blue = [0,0,255]
# pygame.Rect(left, top, width, height): return Rect
rect = pygame.Rect(180, 150, 100, 100)

screen.fill(red)
# pygame.draw.ellipse(Surface, color, Rect, width=0)

e = pygame.draw.line(screen,blue,[50,50], [200,200],10) 

#screen.blit(e, [x,y])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()