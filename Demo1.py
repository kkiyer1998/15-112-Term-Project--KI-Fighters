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
map1=Map()
gk=Goku(gameDisplay,100,100,map1)
while not gameExit:
	if gk.Map.checkcollision((gk.X+gk.dx,gk.Y+gk.dy)):
		if gk.state=="UP" or gk.state=="DOWN":
			gk.dy=-gk.dy
			gk.Y+=gk.dy
			gk.X+=gk.dx
			gk.dy=-gk.dy
		elif gk.state=="LEFT" or gk.state=="RIGHT":
			gk.dx=-gk.dx
			gk.Y+=gk.dy
			gk.X+=gk.dx
			gk.dx=-gk.dx
		gk.state=None
	else:
		gk.Y+=gk.dy
		gk.X+=gk.dx
	gameDisplay.fill(white)
	map1.blitmap(gameDisplay)
	message("Sup Doodes This game is far from done")
	gk.update()
	map1.blittrees(gameDisplay)
	gk.animate()
	for evt in pygame.event.get():
		if evt.type == pygame.QUIT:
			gameExit=True
		gk.Move(evt)
	clock.tick(8)
	pygame.display.flip()
	




pygame.quit()
quit()