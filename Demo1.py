import pygame
from charclass import *
pygame.init()
white = [255,255,255]
gameDisplay = pygame.display.set_mode((1000,500))
pygame.display.set_caption("DEMO 1")
clock = pygame.time.Clock()
bg = pygame.image.load("Images/Map1.png").convert()
char = pygame.image.load("Goku.png").convert()
gameExit = False
gk=Goku(gameDisplay,100,100)
while not gameExit:
	gameDisplay.fill(white)
	#gameDisplay.blit(bg,(0,0))
	gk.update()
	gk.X+=gk.dx
	gk.Y+=gk.dy
	for evt in pygame.event.get():
		if evt.type == pygame.QUIT:
			gameExit=True
		gk.Move(evt)
	clock.tick(13)
	pygame.display.flip()
	




pygame.quit()
quit()