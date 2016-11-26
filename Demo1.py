import pygame
from gameclass import *
from charclass import *
pygame.init()
pygame.mixer.init()

white = [255,255,255]
g=MainGame()
g.menuloop()
(c1,c2) = g.getchars()
pygame.mixer.init()
introsound = pygame.mixer.Sound(file="Sounds/FightSong.wav")
introsound.play()
gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("DEMO 1")
clock = pygame.time.Clock()
gameExit = False
font=pygame.font.SysFont(None,25)
def message(msg):
	text=font.render(msg,True,white)
	gameDisplay.blit(text,(300,300))

map1=Map()
listofki=[]
winner = None



if c1 =="Goku":
        char1=Goku(gameDisplay,200,200,map1,1)
else:
        char1=Vegeta(gameDisplay,200,200,map1,1)

if c2 =="Goku":
        char2=Goku(gameDisplay,800,800,map1,2)
else:
        char2=Vegeta(gameDisplay,800,800,map1,2)






while not gameExit:
        if not pygame.mixer.get_busy():
                introsound.play()
        if char1.state == "PUNCH":
                direc=char1.getreststate()
                if direc == "UP":
                        if char2.X >= char1.X-16 and char2.X <= char1.X+16 and char2.Y <= char1.Y and char2.Y>=char1.Y-35:
                                char2.health -=2
                elif direc == "DOWN":
                        if char2.X >= char1.X-16 and char2.X <= char1.X+16 and char2.Y <= char1.Y+35 and char2.Y>=char1.Y:
                                char2.health -=2
                elif direc == "LEFT":
                        if char2.X >= char1.X and char2.X <= char1.X+35 and char2.Y >= char1.Y-16 and char2.Y <= char1.Y+16:
                                char2.health -= 2
                elif direc == "RIGHT":
                        if char2.X >= char1.X-35 and char2.X <= char1.X and char2.Y >= char1.Y-16 and char2.Y <= char1.Y+16:
                                char2.health -= 2
        if char2.state == "PUNCH":
                direc=char2.getreststate()
                if direc == "UP":
                        if char1.X >= char2.X-16 and char1.X <= char2.X+16 and char1.Y <= char2.Y and char1.Y>=char2.Y-35:
                                char1.health -=2
                elif direc == "DOWN":
                        if char1.X >= char2.X-16 and char1.X <= char2.X+16 and char1.Y <= char2.Y+35 and char1.Y>=char2.Y:
                                char1.health -=2
                elif direc == "LEFT":
                        if char1.X >= char2.X and char1.X <= char2.X+35 and char1.Y >= char2.Y-16 and char1.Y <= char2.Y+16:
                                char1.health -= 2
                elif direc == "RIGHT":
                        if char1.X >= char2.X-35 and char1.X <= char2.X and char1.Y >= char2.Y-16 and char1.Y <= char2.Y+16:
                                char1.health -= 2

                        
                        
        if char1.state == "KI":
                char1.kiamt -= 20
                if char1.state1 == None:
                        if char1.curpic == char1.uki:
                                state = "UP"
                        elif char1.curpic == char1.dki:
                                state = "DOWN"
                        elif char1.curpic == char1.rki:
                                state = "RIGHT"
                        else:
                                state = "LEFT"
                else:
                        state = char1.state1
                listofki.append(Ki(char1.X,char1.Y,state,gameDisplay))
                
        if char2.state == "KI":
                char2.kiamt -= 20
                if char2.state1 == None:
                        if char2.curpic == char2.uki:
                                state = "UP"
                        elif char2.curpic == char2.dki:
                                state = "DOWN"
                        elif char2.curpic == char2.rki:
                                state = "RIGHT"
                        else:
                                state = "LEFT"
                else:
                        state = char2.state1
                listofki.append(Ki(char2.X,char2.Y,state,gameDisplay))

        
                        
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
        char1.update()
        char2.update()
        map1.blitobstacles(gameDisplay)
        pygame.draw.rect(char1.window,char1.healthcolor,(char1.hloc[0],char1.hloc[1],char1.health,20))
        pygame.draw.rect(char1.window,char1.kicolor,(char1.kiloc[0],char1.kiloc[1],char1.kiamt,20))
        pygame.draw.rect(char2.window,char2.healthcolor,(char2.hloc[0],char2.hloc[1],char2.health,20))
        pygame.draw.rect(char2.window,char2.kicolor,(char2.kiloc[0],char2.kiloc[1],char2.kiamt,20))
	
        char2.animate()
        char1.animate()
        for i in listofki:
                g = i.checkcollisions(map1,char1,char2)
                if not (g == False or g == map1):
                        g.health -= 15
                i.animate()
        for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                        gameExit=True
                char1.Move(evt)
                char2.Move(evt)
        if char1.health <= 0:
                winner = char2
                introsound.stop()
                gameExit = True
        if char2.health <= 0:
                winner = char1
                introsound.stop()
                gameExit = True
        clock.tick(8)
        pygame.display.flip()



pygame.quit()
quit()
