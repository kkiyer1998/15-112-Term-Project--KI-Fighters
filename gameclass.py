##############################################################################
##############################################################################
##########################  MAIN MENU CLASS DEFS  ############################
##############################################################################
##############################################################################

###########################  IMPORTING MODULES  ##############################
import pygame
from charclass import *
pygame.init()
pygame.mixer.init()
##############################################################################

################################ CLASS DEFS ##################################
class MainGame:
    def __init__(self):
        #Window, time, sound, and other important stuff
        self.gamedisplay = pygame.display.set_mode((1000,750))
        self.clock = pygame.time.Clock()
        

        #Main Menu related stuff
        self.mainloop = True
        self.inmenu = True
        self.ininstr = False
        self.instart = False
        self.menuimg = pygame.image.load("menupic.jpg").convert()
        self.menux = 1000
        self.menuy = 1000
        self.menudx = -10
        self.menudy = -10
        self.textbox = None

        #BUTTONS AND CHOICES
        self.buttonimg = pygame.image.load("Images/button.png").convert()
        self.litbuttonimg = pygame.image.load("Images/buttonlit.png").convert()
        self.startgame = self.buttonimg
        self.start = self.buttonimg
        self.instructions = self.buttonimg
        self.quit = self.buttonimg
        self.back = self.buttonimg
        self.goku = self.buttonimg
        self.vegeta = self.buttonimg
        self.curplayer = 0
        self.player1 = None
        self.player2 = None
        
        #SOUND AND TEXT
        self.font = pygame.font.SysFont(None,25)
        self.font1 = pygame.font.SysFont(None,40)
        self.introsound = pygame.mixer.Sound(file="Sounds/Intro.wav")
        self.introsound.play()
        self.buttonhover = pygame.mixer.Sound(file="Sounds/Button.wav")


    def message(self,msg,x,y):#DISPLAYS TEXT ON A SCREEN(FOR BUTTONS)
        text=self.font.render(msg,True,[0,0,0])
        self.gamedisplay.blit(text,(x,y))
            
    def lightitup(self,(x,y)):#LIGHTS UP BUTTONS ON HOVER
        if self.inmenu:
            if x > 400 and x < 600:
                if y > 300 and y < 350:
                    if self.startgame == self.buttonimg:
                        self.buttonhover.play()
                    self.startgame = self.litbuttonimg
                elif y > 400 and y < 450:
                    if self.instructions == self.buttonimg:
                        self.buttonhover.play()
                    self.instructions = self.litbuttonimg
                elif y > 500 and y < 550:
                    if self.quit == self.buttonimg:
                        self.buttonhover.play()
                    self.quit = self.litbuttonimg
                else:
                    if self.startgame == self.litbuttonimg  or  self.instructions == self.litbuttonimg  or  self.quit == self.litbuttonimg:
                        self.buttonhover.play()
                    self.startgame = self.buttonimg
                    self.instructions = self.buttonimg
                    self.quit = self.buttonimg
        elif self.ininstr:
            if x > 400 and x < 600:
                if y > 680 and y < 730:
                    if self.back == self.buttonimg:
                        self.buttonhover.play()
                    self.back = self.litbuttonimg
                else:
                    if self.back == self.litbuttonimg:
                        self.buttonhover.play()
                    self.back = self.buttonimg
        elif self.instart:
            if x > 400 and x < 600:
                if y > 600 and y <650:
                    if self.goku == self.buttonimg:
                        self.buttonhover.play()
                    self.goku = self.litbuttonimg
                elif y > 680 and y < 730:
                    if self.vegeta == self.buttonimg:
                        self.buttonhover.play()
                    self.vegeta = self.litbuttonimg
                else:
                    if self.vegeta == self.litbuttonimg or self.goku == self.litbuttonimg:
                        self.buttonhover.play()
                    self.goku = self.buttonimg
                    self.vegeta = self.buttonimg

    # from- http://www.pygame.org/wiki/TextWrap
    def drawText(self,surface, text, color, rect, font, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2
        # get the height of the font
        fontHeight = font.size("Tg")[1]
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]
        return text

    
    #CALLED ON CLICKING A BUTTON
    def openit(self,(x,y)):
        if self.inmenu:
            if x > 400 and x < 600:
                if y > 300 and y < 350:
                    self.inmenu = False
                    self.instart = True
                elif y > 400 and y < 450:
                    self.inmenu = False
                    self.ininstr = True
                elif y > 500 and y < 550:
                    self.mainloop = False
                    pygame.quit()
                    quit()
                    
        elif self.ininstr:
            if x > 400 and x < 600:
                if y > 680 and y < 730:
                    self.ininstr = False
                    self.inmenu = True
        elif self.instart:
            if x > 400 and x < 600:
                if y > 600 and y <650:
                    if self.curplayer == 0:
                        self.player1 = "Goku"
                        self.curplayer += 1
                    elif self.curplayer == 1:
                        self.player2 = "Goku"
                        self.mainloop = False
                elif y > 680 and y < 730:
                    if self.curplayer == 0:
                        self.player1 = "Vegeta"
                        self.curplayer += 1
                    elif self.curplayer == 1:
                        self.player2 = "Vegeta"
                        self.mainloop = False

    #RETURNS A TUPLE WITH USER-SELECTED CHARACTERS
    def getchars(self):
        return (self.player1,self.player2)


    #CALLS THE LOOP OF THE MAIN MENU 
    def menuloop(self):
        black = [0,0,0]
        if not pygame.mixer.get_busy():
            self.introsound.play()
        
        while self.mainloop:
            if not pygame.mixer.get_busy():
                self.introsound.play()
            #MAIN SCREEN
            if self.inmenu:
                        
                pygame.display.set_caption(str(self.clock.get_fps()))
                self.gamedisplay.fill(black)
                self.gamedisplay.blit(self.menuimg,(self.menux,self.menuy))

                self.menux += self.menudx
                self.menuy += self.menudy
                if self.menux <= 0 or self.menuy <= 0:
                    self.menudx = 0
                    self.menudy = 0
                    self.menux = 0
                    self.menuy = 0
                    self.gamedisplay.blit(self.startgame,(400,300))
                    self.gamedisplay.blit(self.instructions,(400,400))
                    self.gamedisplay.blit(self.quit,(400,500))
                    self.message("Start Game",450,315)
                    self.message("Instructions",450,415)
                    self.message("Quit",480,515)

                for evt in pygame.event.get():
                    if evt.type == pygame.MOUSEMOTION:
                        self.lightitup(evt.pos)
                    if evt.type == pygame.QUIT  or  (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
                        pygame.mixer.quit()
                        pygame.quit()
                        quit()
                    if evt.type == pygame.MOUSEBUTTONUP:
                        self.openit(evt.pos)
                self.clock.tick(60)
                pygame.display.flip()




            #INSTRUCTION SCREEN
            if self.ininstr:
                manual = "Welcome to KI Fighters- A 2-player 2D topdown fighter game. You get to choose between Goku and Vegito and fight each other in a duel unto death. Player 1 uses W, A, S and D to move up, left, down and right respectively. R is to Punch and T enables a long range energy blast. Player 2 will have the directional keys for movements, and P to punch and O for the energy blast.First player down to zero HP wins! Keep in mind that using KI blasts drains your energy bar! Thanks and enjoy"
                pygame.display.set_caption(str(self.clock.get_fps()))
                self.gamedisplay.fill(black)
                self.gamedisplay.blit(self.menuimg,(self.menux,self.menuy))
                self.textbox = pygame.draw.rect(self.gamedisplay,[100,100,100],(100,150,800,500))
                self.drawText(self.gamedisplay,manual,[255,0,0],self.textbox,self.font1)
                self.gamedisplay.blit(self.back,(400,680))
                self.message("Back",480,695)
                for evt in pygame.event.get():
                    if evt.type == pygame.MOUSEMOTION:
                        self.lightitup(evt.pos)
                    if evt.type == pygame.QUIT  or  (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
                        pygame.mixer.quit()
                        pygame.quit()
                        quit()
                    if evt.type == pygame.MOUSEBUTTONUP:
                        self.openit(evt.pos)

                self.clock.tick(60)
                pygame.display.flip()




            #START GAME SCREEN
            if self.instart:
                pygame.display.set_caption(str(self.clock.get_fps()))
                self.gamedisplay.fill(black)
                self.gamedisplay.blit(self.menuimg,(self.menux,self.menuy))
                self.gamedisplay.blit(self.goku,(400,600))
                self.gamedisplay.blit(self.vegeta,(400,680))
                fnt = pygame.font.SysFont(None,40)
                text = fnt.render("Choose Your Player- Player "+ str(self.curplayer+1),True,[255,0,0])
                self.gamedisplay.blit(text,(350,200))
                
                self.message("Goku",475,615)
                self.message("Vegeta",480,695)
                for evt in pygame.event.get():
                    if evt.type == pygame.MOUSEMOTION:
                        self.lightitup(evt.pos)
                    if evt.type == pygame.QUIT  or  (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
                        self.instart = False
                        self.mainloop = False
                    if evt.type == pygame.MOUSEBUTTONUP:
                        self.openit(evt.pos)


                self.clock.tick(60)
                pygame.display.flip()
        pygame.mixer.quit()

            

        return None
