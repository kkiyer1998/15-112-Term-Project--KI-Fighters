import pygame
from charclass import *
pygame.init()
white = [255,255,255]
gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("DEMO 1")
clock = pygame.time.Clock()
bg = pygame.image.load("Images/Map1.png").convert()
char = pygame.image.load("Goku.png").convert()
gameExit = False
font=pygame.font.SysFont(None,25)
def message(msg):
	text=font.render(msg,True,white)
	gameDisplay.blit(text,(300,300))
gk=Goku(gameDisplay,100,100)
map1=Map()
while not gameExit:
	gameDisplay.fill(white)
	map1.blitmap(gameDisplay)
	message("Sup Doodes This game is far from done")
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