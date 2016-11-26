#KKIYER@ANDREW.CMU.EDU#
####################################################################################
############################IMPORTING USED MODULES##################################
####################################################################################


import pygame
from PIL import Image
import random


####################################################################################
#############################CLASS DEFINITIONS######################################
####################################################################################


#### My map is basically a 20X20 grid of 50X50 px per part.
# It consists of trees in addition that are spawned at a random
# number in random places(grid locations). These trees are, of course
# Non-collideable, and a function handles it with an object location
# and the set of grid co-ordinates of the trees(defined in init) 
class Map:#Generates a map with a random number of trees at random locations
	def __init__(self):#constructor
		self.nooftrees=random.randint(10,15)#No. of trees is randomized
		self.treelocs=[]
		self.imgs=[None]*400
		for i in range(self.nooftrees):#togive all trees random locations
			self.treelocs.append((random.randint(0,20),random.randint(0,20)))
		self.initmap()
	def checkcollision(self,(x,y)):#For collision handling
                if x>=1000 or x<=0 or y>=1000 or y<=0:
                        return True
		x=x/50
		y=y/50
		if (x,y) in self.treelocs:
			return True
		return False
	def loadimg(self,file):#loads the spawnable images(50X50)
		if 'tree' in file:
			image=pygame.image.load(file).convert_alpha()
		else:
			image=pygame.image.load(file).convert()
		return image
	def initmap(self):#Uses images to spawn the map(as a list)
		x=0
		for i in range(20):
			for j in range(20):
				if (i,j) in self.treelocs:
					self.imgs[x]=self.loadimg("Images/tree.png")
				else:
					self.imgs[x]=self.loadimg("Images/ground.png")
				x+=1
	def blitmap(self,wind):#blits map on screen
		i=0
		j=0
		x=0
		while i<1000:
			while j<1000:
				wind.blit(self.loadimg("Images/ground.png"),[i,j])
				x+=1
				j+=50
			i+=50
			j=0
	def blitobstacles(self,wind):
		i=0
		j=0
		x=0
		while i<1000:
			while j<1000:
				if (i/50,j/50) in self.treelocs:
					wind.blit(self.imgs[x],[i,j])
				x+=1
				j+=50
			i+=50
			j=0



class Goku:
	def getImgLib(self):
		lib=[]
		for i in range(125):
			lib.append(pygame.image.load("Images/Goku"+str(i)+".png").convert_alpha())
		return lib


	def __init__(self,window,x,y,Map,player):
		self.image_lib = self.getImgLib()

		self.state = None
		self.state1 = None

		self.X = x
		self.Y = y
		self.dx = 0
		self.dy = 0
		self.dx1 = 0
		self.dy1 = 0

		self.curpic = 17
		self.nextpic = ""
		self.uppic = 18
		self.downpic = 17
		self.rpic = 19
		self.lpic = 20
		self.ppic = 0
		self.uppunch = 46
		self.downpunch = 45
		self.rpunch = 47
		self.lpunch = 48
		self.uki = 102
		self.dki = 101
		self.rki = 103
		self.lki = 104
		self.countpunch = 0

		self.Map = Map	
		self.window = window
		self.window.blit(self.image_lib[1],(x,y))

		self.health = 200
		self.kiamt = 200
		self.healthcolor = [0,0,255]
		self.kicolor = [0,255,0]
		if player == 1:
			self.hloc = [20,20]
			self.kiloc = [20,40]
		else:
			self.hloc = [780,20]
			self.kiloc = [780,40]
		pygame.draw.rect(self.window,self.healthcolor,(self.hloc[0],self.hloc[1],self.health,20))
		pygame.draw.rect(self.window,self.kicolor,(self.kiloc[0],self.kiloc[1],self.kiamt,20))


		if player == 1:
			self.up = pygame.K_w
			self.down = pygame.K_s
			self.left = pygame.K_a
			self.right = pygame.K_d
			self.punch = pygame.K_r
			self.ki = pygame.K_t
		else:
			self.up = pygame.K_UP
			self.down = pygame.K_DOWN
			self.left = pygame.K_LEFT
			self.right = pygame.K_RIGHT
			self.punch = pygame.K_p
			self.ki = pygame.K_o

	def checkcollision(self,x,y):
		if (x>self.X and x<self.X+32) and (y>self.Y and y<self.Y+32):
			return True

	def update(self):
		self.window.blit(self.image_lib[self.curpic],(self.X,self.Y))
		pygame.draw.rect(self.window,self.healthcolor,(self.hloc[0],self.hloc[1],self.health,20))
		pygame.draw.rect(self.window,self.kicolor,(self.kiloc[0],self.kiloc[1],self.kiamt,20))



	def animate(self):#Called every frame
		if self.state != None  and  self.state != "PUNCH"  and  self.state != "KI":
			if self.curpic > 36:
				if self.state == "UP":
					self.curpic = self.uppic
				elif self.state == "DOWN":
					self.curpic = self.downpic
				elif self.state == "RIGHT":
					self.curpic = self.rpic
				elif self.state == "LEFT":
					self.curpic = self.lpic
			self.curpic += 4
		elif self.state == "KI":
			self.curpic+=4
			self.state = self.state1
			self.state1 = "KI"
		elif self.state == "PUNCH":
			self.curpic += 4
			self.countpunch += 1
			if (self.curpic >= self.downpunch + 12 and self.state1 == "DOWN") or (self.curpic >= self.uppunch + 12 and self.state1 == "UP") or (self.curpic >= self.lpunch + 12 and self.state1 == "LEFT") or (self.curpic >= self.rpunch + 12 and self.state1 == "RIGHT") or self.countpunch == 3:
                                self.countpunch = 0
				self.dx = self.dx1
				self.dy = self.dy1
				self.state = self.state1
				if self.state == "UP":
					self.curpic = self.uppic
				elif self.state == "DOWN":
					self.curpic = self.downpic
				elif self.state == "RIGHT":
					self.curpic = self.rpic
				elif self.state == "LEFT":
					self.curpic = self.lpic
				elif self.state == None:
					if self.curpic == self.downpunch + 12:
						self.curpic = self.downpic
					elif self.curpic == self.uppunch + 12:
						self.curpic = self.uppic
					elif self.curpic == self.rpunch + 12:
						self.curpic = self.rpic
					elif self.curpic == self.lpunch + 12:
						self.curpic = self.lpic
		if self.state1 == "KI":
                        self.state1 = None
                        self.dx = self.dx1
                        self.dy = self.dy1
                        if self.state == "UP":
                                self.curpic = self.uppic
                        elif self.state == "DOWN":
                                self.curpic = self.downpic
                        elif self.state == "LEFT":
                                self.curpic = self.lpic
                        elif self.state == "RIGHT":
                                self.curpic = self.rpic
                        elif self.curpic == self.uki + 4:
                                self.curpic = self.uppic
                        elif self.curpic == self.dki + 4:
                                self.curpic = self.downpic
                        elif self.curpic == self.lki + 4:
                                self.curpic = self.lpic
                        elif self.curpic == self.rki + 4:
                                self.curpic = self.rpic
                                

        def getreststate(self):
                if self.curpic%4 == 1:
                        return "DOWN"
                elif self.curpic%4 == 2:
                        return "UP"
                elif self.curpic%4 == 3:
                        return "LEFT"
                else:
                        return "RIGHT"

	def Move(self,evt):
		if evt.type == pygame.KEYDOWN:
			if evt.key == self.up:
				if self.state == None  or  self.state == "DOWN":
					self.state = "UP"
					self.curpic = self.uppic
				else:
					self.state1 = "UP"
				self.dy = -10


			if evt.key == self.left:
				if self.state == None  or  self.state == "RIGHT":
					self.state = "LEFT"
					self.curpic = self.lpic
				else:
					self.state1 = "LEFT"
				self.dx = -10


			if evt.key == self.down:
				if self.state == None  or  self.state == "UP":
					self.state = "DOWN"
					self.curpic = self.downpic
				else:
					self.state1 = "DOWN"
				self.dy = 10


			if evt.key == self.right:
				if self.state == None  or  self.state == "LEFT":
					self.state = "RIGHT"
					self.curpic = self.rpic
				else:
					self.state1 = "RIGHT"
				self.dx = 10


			if evt.key == self.punch:
				self.dx1 = self.dx
				self.dy1 = self.dy
				self.dx = 0
				self.dy = 0
				self.downpunch = random.choice([45,57,69])
				self.uppunch = random.choice([46,58,70])
				self.rpunch = random.choice([47,59,71])
				self.lpunch = random.choice([49,60,72])
				if self.state == None:
					self.state1 = None
					self.state = "PUNCH"
					if self.curpic == self.uppic:
						self.curpic = self.uppunch	
					elif self.curpic == self.downpic:
						self.curpic = self.downpunch
					elif self.curpic == self.lpic:
						self.curpic = self.lpunch
					elif self.curpic == self.rpic:
						self.curpic = self.rpunch
				if self.state == "UP":
					self.curpic = self.uppunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "DOWN":
					self.curpic = self.downpunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "LEFT":
					self.curpic = self.lpunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "RIGHT":
					self.curpic = self.rpunch
					self.state1 = self.state
					self.state = "PUNCH"


			if evt.key == self.ki:
				self.dx1 = self.dx
				self.dy1 = self.dy
				self.dx = 0
				self.dy = 0
				if self.state == None:
					self.state1 = None
					self.state = "KI"
					if self.curpic == self.uppic:
						self.curpic = self.uki	
					elif self.curpic == self.downpic:
						self.curpic = self.dki
					elif self.curpic == self.lpic:
						self.curpic = self.lki
					elif self.curpic == self.rpic:
						self.curpic = self.rki
				if self.state == "UP":
					self.state1 = "UP"
					self.state = "KI"
					self.curpic = self.uki
				elif self.state == "DOWN":
					self.state1 = "DOWN"
					self.state = "KI"
					self.curpic = self.dki
				elif self.state == "LEFT":
					self.state1 = "LEFT"
					self.state = "KI"
					self.curpic = self.lki
				elif self.state == "RIGHT":
					self.state1 = "RIGHT"
					self.state = "KI"
					self.curpic = self.rki



		elif evt.type == pygame.KEYUP:
			if evt.key == self.up:
				if self.state == "UP":
					self.curpic = self.uppic
					self.state = None
				if self.state1 == "RIGHT"  or  self.state1 == "LEFT":
					self.state = self.state1
					self.state1 = None
					if self.state == "RIGHT": self.curpic = self.rpic
					else: self.curpic = self.lpic
				self.dy = 0
			if evt.key == self.left:
				if self.state == "LEFT":
					self.curpic = self.lpic
					self.state = None
				if self.state1 == "UP"  or  self.state1 == "DOWN":
					self.state = self.state1
					self.state1 = None

					if self.state == "UP": self.curpic = self.uppic
					else: self.curpic = self.downpic
				self.dx = 0
			if evt.key == self.down:
				if self.state == "DOWN":
					self.curpic = self.downpic
					self.state = None
				if self.state1 == "RIGHT"  or  self.state1 == "LEFT":
					self.state = self.state1
					self.state1 = None

					if self.state == "RIGHT": self.curpic = self.rpic
					else: self.curpic = self.lpic

				self.dy = 0
			if evt.key == self.right:
				if self.state == "RIGHT":
					self.curpic = self.rpic
					self.state = None
				if self.state1 == "UP"  or  self.state1 == "DOWN":
					self.state = self.state1

					if self.state == "UP": self.curpic = self.uppic
					else: self.curpic = self.downpic

					self.state1 = None
				self.dx = 0


				
class Ki:
        def __init__(self,x,y,direc,window):
                self.images = []
                for i in range(6):
                        self.images.append(pygame.image.load("Images/ki"+str(i)+".png").convert_alpha())
                self.hascollided = False
                self.end = False
                self.curpic = 0
                self.x = x
                self.y = y
                self.dx = 0
                self.dy = 0
                self.wnd = window
                self.direc = direc
                if direc == "UP":
                        self.y -= 5 
                        self.dy = -15
                elif direc == "DOWN":
                        self.y += 38
                        self.dy = 15
                elif direc == "RIGHT":
                        self.x += 38
                        self.dx = 15
                elif direc == "LEFT":
                        self.x -= 5
                        self.dx = -15
                self.wnd.blit(self.images[0],(self.x,self.y))
        def checkcollisions(self,Map,p1,p2):
                a = self.x/50
		b = self.y/50
		if (a,b) in Map.treelocs:
                        self.hascollided = True
			return Map
                if (self.x>=p1.X and self.x<=p1.X+32) and (self.y>=p1.Y and self.y<=p1.Y+32):
                        print "hey", self.x,p2.X,"sup", self.y, p2.Y
                        self.hascollided = True
                        return p1
                if (self.x>=p2.X and self.x<=p2.X+32) and (self.y>=p2.Y and self.y<=p2.Y+32):
                        print "hey", self.x,p2.X,"sup", self.y, p2.Y
                        self.hascollided = True
                        return p2
		return False
                
        def animate(self):
                if self.hascollided:
                        if not self.end:
                                self.wnd.blit(self.images[5],(self.x,self.y))
                                self.end = True
                else:
                        self.wnd.blit(self.images[self.curpic],(self.x,self.y))
                self.x += self.dx
                self.y += self.dy
                if self.curpic < 3:
                        self.curpic += 1



class Vegeta:
	def getImgLib(self):
		lib=[]
		for i in range(125):
			lib.append(pygame.image.load("Images/Vegeta"+str(i)+".png").convert_alpha())
		return lib


	def __init__(self,window,x,y,Map,player):
		self.image_lib = self.getImgLib()

		self.state = None
		self.state1 = None

		self.X = x
		self.Y = y
		self.dx = 0
		self.dy = 0
		self.dx1 = 0
		self.dy1 = 0

		self.curpic = 1
		self.nextpic = ""
		self.uppic = 2
		self.downpic = 1
		self.rpic = 3
		self.lpic = 4
		self.ppic = 0
		self.uppunch = 34
		self.downpunch = 33
		self.rpunch = 35
		self.lpunch = 36
		self.uki = 66
		self.dki = 65
		self.rki = 67
		self.lki = 68
		self.countpunch = 0

		self.Map = Map	
		self.window = window
		self.window.blit(self.image_lib[1],(x,y))

		self.health = 200
		self.kiamt = 200
		self.healthcolor = [0,0,255]
		self.kicolor = [0,255,0]
		if player == 1:
			self.hloc = [20,20]
			self.kiloc = [20,40]
		else:
			self.hloc = [780,20]
			self.kiloc = [780,40]
		pygame.draw.rect(self.window,self.healthcolor,(self.hloc[0],self.hloc[1],self.health,20))
		pygame.draw.rect(self.window,self.kicolor,(self.kiloc[0],self.kiloc[1],self.kiamt,20))


		if player == 1:
			self.up = pygame.K_w
			self.down = pygame.K_s
			self.left = pygame.K_a
			self.right = pygame.K_d
			self.punch = pygame.K_r
			self.ki = pygame.K_t
		else:
			self.up = pygame.K_UP
			self.down = pygame.K_DOWN
			self.left = pygame.K_LEFT
			self.right = pygame.K_RIGHT
			self.punch = pygame.K_p
			self.ki = pygame.K_o

	def checkcollision(self,x,y):
		if (x>self.X and x<self.X+32) and (y>self.Y and y<self.Y+32):
			return True

	def update(self):
		self.window.blit(self.image_lib[self.curpic],(self.X,self.Y))
		


        def getreststate(self):
                if self.curpic%4 == 1:
                        return "DOWN"
                elif self.curpic%4 == 2:
                        return "UP"
                elif self.curpic%4 == 3:
                        return "LEFT"
                else:
                        return "RIGHT"

                
	def animate(self):#Called every frame
		if self.state != None  and  self.state != "PUNCH"  and  self.state != "KI":
			if self.curpic > 28:
				if self.state == "UP":
					self.curpic = self.uppic
				elif self.state == "DOWN":
					self.curpic = self.downpic
				elif self.state == "RIGHT":
					self.curpic = self.rpic
				elif self.state == "LEFT":
					self.curpic = self.lpic
			self.curpic += 4
		elif self.state == "KI":
			self.curpic+=4
			self.state = self.state1
			self.state1 = "KI"
		elif self.state == "PUNCH":
			self.curpic += 4
			self.countpunch += 1

			if (self.curpic >= self.downpunch + 8 and self.state1 == "DOWN") or (self.curpic >= self.uppunch + 8 and self.state1 == "UP") or (self.curpic >= self.lpunch + 8 and self.state1 == "LEFT") or (self.curpic >= self.rpunch + 8 and self.state1 == "RIGHT") or self.countpunch == 2:
                                self.countpunch = 0
				self.dx = self.dx1
				self.dy = self.dy1
				self.state = self.state1
				if self.state == "UP":
					self.curpic = self.uppic
				elif self.state == "DOWN":
					self.curpic = self.downpic
				elif self.state == "RIGHT":
					self.curpic = self.rpic
				elif self.state == "LEFT":
					self.curpic = self.lpic
				elif self.state == None:
					if self.curpic == self.downpunch + 8:
						self.curpic = self.downpic
					elif self.curpic == self.uppunch + 8:
						self.curpic = self.uppic
					elif self.curpic == self.rpunch + 8:
						self.curpic = self.rpic
					elif self.curpic == self.lpunch + 8:
						self.curpic = self.lpic
			 
		if self.state1 == "KI":
                        self.state1 = None
                        self.dx = self.dx1
                        self.dy = self.dy1
                        if self.state == "UP":
                                self.curpic = self.uppic
                        elif self.state == "DOWN":
                                self.curpic = self.downpic
                        elif self.state == "LEFT":
                                self.curpic = self.lpic
                        elif self.state == "RIGHT":
                                self.curpic = self.rpic
                        elif self.curpic == self.uki + 4:
                                self.curpic = self.uppic
                        elif self.curpic == self.dki + 4:
                                self.curpic = self.downpic
                        elif self.curpic == self.lki + 4:
                                self.curpic = self.lpic
                        elif self.curpic == self.rki + 4:
                                self.curpic = self.rpic
                                



	def Move(self,evt):
		if evt.type == pygame.KEYDOWN:
			if evt.key == self.up:
				if self.state == None  or  self.state == "DOWN":
					self.state = "UP"
					self.curpic = self.uppic
				else:
					self.state1 = "UP"
				self.dy = -10


			if evt.key == self.left:
				if self.state == None  or  self.state == "RIGHT":
					self.state = "LEFT"
					self.curpic = self.lpic
				else:
					self.state1 = "LEFT"
				self.dx = -10


			if evt.key == self.down:
				if self.state == None  or  self.state == "UP":
					self.state = "DOWN"
					self.curpic = self.downpic
				else:
					self.state1 = "DOWN"
				self.dy = 10


			if evt.key == self.right:
				if self.state == None  or  self.state == "LEFT":
					self.state = "RIGHT"
					self.curpic = self.rpic
				else:
					self.state1 = "RIGHT"
				self.dx = 10


			if evt.key == self.punch:
				self.dx1 = self.dx
				self.dy1 = self.dy
				self.dx = 0
				self.dy = 0
				self.downpunch = random.choice([33,41,49])
				self.uppunch = random.choice([34,42,50])
				self.rpunch = random.choice([35,43,51])
				self.lpunch = random.choice([36,44,52])
				if self.state == None:
					self.state1 = None
					self.state = "PUNCH"
					if self.curpic == self.uppic:
						self.curpic = self.uppunch	
					elif self.curpic == self.downpic:
						self.curpic = self.downpunch
					elif self.curpic == self.lpic:
						self.curpic = self.lpunch
					elif self.curpic == self.rpic:
						self.curpic = self.rpunch
				if self.state == "UP":
					self.curpic = self.uppunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "DOWN":
					self.curpic = self.downpunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "LEFT":
					self.curpic = self.lpunch
					self.state1 = self.state
					self.state = "PUNCH"
				elif self.state == "RIGHT":
					self.curpic = self.rpunch
					self.state1 = self.state
					self.state = "PUNCH"


			if evt.key == self.ki:
				self.dx1 = self.dx
				self.dy1 = self.dy
				self.dx = 0
				self.dy = 0
				if self.state == None:
					self.state1 = None
					self.state = "KI"
					if self.curpic == self.uppic:
						self.curpic = self.uki	
					elif self.curpic == self.downpic:
						self.curpic = self.dki
					elif self.curpic == self.lpic:
						self.curpic = self.lki
					elif self.curpic == self.rpic:
						self.curpic = self.rki
				if self.state == "UP":
					self.state1 = "UP"
					self.state = "KI"
					self.curpic = self.uki
				elif self.state == "DOWN":
					self.state1 = "DOWN"
					self.state = "KI"
					self.curpic = self.dki
				elif self.state == "LEFT":
					self.state1 = "LEFT"
					self.state = "KI"
					self.curpic = self.lki
				elif self.state == "RIGHT":
					self.state1 = "RIGHT"
					self.state = "KI"
					self.curpic = self.rki



		elif evt.type == pygame.KEYUP:
			if evt.key == self.up:
				if self.state == "UP":
					self.curpic = self.uppic
					self.state = None
				if self.state1 == "RIGHT"  or  self.state1 == "LEFT":
					self.state = self.state1
					self.state1 = None
					if self.state == "RIGHT": self.curpic = self.rpic
					else: self.curpic = self.lpic
				self.dy = 0
			if evt.key == self.left:
				if self.state == "LEFT":
					self.curpic = self.lpic
					self.state = None
				if self.state1 == "UP"  or  self.state1 == "DOWN":
					self.state = self.state1
					self.state1 = None

					if self.state == "UP": self.curpic = self.uppic
					else: self.curpic = self.downpic
				self.dx = 0
			if evt.key == self.down:
				if self.state == "DOWN":
					self.curpic = self.downpic
					self.state = None
				if self.state1 == "RIGHT"  or  self.state1 == "LEFT":
					self.state = self.state1
					self.state1 = None

					if self.state == "RIGHT": self.curpic = self.rpic
					else: self.curpic = self.lpic

				self.dy = 0
			if evt.key == self.right:
				if self.state == "RIGHT":
					self.curpic = self.rpic
					self.state = None
				if self.state1 == "UP"  or  self.state1 == "DOWN":
					self.state = self.state1

					if self.state == "UP": self.curpic = self.uppic
					else: self.curpic = self.downpic

					self.state1 = None
				self.dx = 0
                
                
                
                
                
                
