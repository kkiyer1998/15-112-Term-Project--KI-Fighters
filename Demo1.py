import pygame
from charclass import *
pygame.init()
white = [255,255,255]
gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("DEMO 1")
clock = pygame.time.Clock()
menubg = pygame.image.load("menupic.jpg").convert()
char = pygame.image.load("Goku.png").convert()
gameExit = False
font=pygame.font.SysFont(None,25)
def message(msg):
	text=font.render(msg,True,white)
	gameDisplay.blit(text,(300,300))
started=2
map1=Map()
char1=Goku(gameDisplay,100,100,map1,1)
char2=Goku(gameDisplay,200,200,map1,2)
while not gameExit:
	if started==2:
		if char2.Map.checkcollision((char2.X+char2.dx,char2.Y+char2.dy)):
			if char2.state=="UP" or char2.state=="DOWN":
				char2.dy=-char2.dy
				char2.Y+=char2.dy
				char2.X+=char2.dx
				char2.dy=-char2.dy
			elif char2.state=="LEFT" or char2.state=="RIGHT":
				char2.dx=-char2.dx
				char2.Y+=char2.dy
				char2.X+=char2.dx
				char2.dx=-char2.dx
			char2.state=None
		else:
			char2.Y+=char2.dy
			char2.X+=char2.dx
		if char1.Map.checkcollision((char1.X+char1.dx,char1.Y+char1.dy)):
			if char1.state=="UP" or char1.state=="DOWN":
				char1.dy=-char1.dy
				char1.Y+=char1.dy
				char1.X+=char1.dx
				char1.dy=-char1.dy
			elif char1.state=="LEFT" or char1.state=="RIGHT":
				char1.dx=-char1.dx
				char1.Y+=char1.dy
				char1.X+=char1.dx
				char1.dx=-char1.dx
			char1.state=None
		else:
			char1.Y+=char1.dy
			char1.X+=char1.dx
		gameDisplay.fill(white)
		map1.blitmap(gameDisplay)
		message("Sup Doodes This game is far from done")
		char1.update()
		char2.update()
		map1.blittrees(gameDisplay)
		char2.animate()
		char1.animate()
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT:
				gameExit=True
			char1.Move(evt)
			char2.Move(evt)
	elif started==0:
		gameDisplay.fill(white)
		gameDisplay.blit(menubg,(0,0))
	clock.tick(8)
	pygame.display.flip()



pygame.quit()
quit()