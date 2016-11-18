

#######################IMPORTING USED MODULES##################
import pygame
from PIL import Image
import random

################################################################
#####################CLASS DEFINITIONS##########################
################################################################
#### My map is basically a 20X20 grid of 50X50 px per part.
# It consists of trees in addition that are spawned in a random
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
	def blittrees(self,wind):
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
	def getImgLib(self,file):
		lib=[]
		for i in range(125):
			lib.append(pygame.image.load("Images/Goku"+str(i)+".png").convert_alpha())
		return lib


	def __init__(self,window,x,y,Map):
		self.image_lib=self.getImgLib("Goku.png")
		self.state=None
		self.state1=None
		self.X=x
		self.Map=Map
		self.Y=y
		self.dx=0
		self.dy=0
		self.curpic=1
		self.nextpic=""
		self.uppic=18
		self.downpic=17
		self.rpic=19
		self.lpic=20
		self.ppic=0
		self.window=window
		self.window.blit(self.image_lib[1],(x,y))


	def update(self):
		self.window.blit(self.image_lib[self.curpic],(self.X,self.Y))
	def animate(self):#Called every frame
		if self.state!=None:
			if self.curpic>36:
				if self.state=="UP":
					self.curpic=self.uppic
				elif self.state=="DOWN":
					self.curpic=self.downpic
				elif self.state=="RIGHT":
					self.curpic=self.rpic
				elif self.state=="LEFT":
					self.curpic=self.lpic
			self.curpic+=4
	def Move(self,evt):
		if evt.type == pygame.KEYDOWN:
			if evt.key == pygame.K_w:
				if self.state==None or self.state=="DOWN":
					self.state="UP"
					self.curpic=self.uppic
				else:
					self.state1="UP"
				self.dy=-10
			if evt.key == pygame.K_a:
				if self.state==None or self.state=="RIGHT":
					self.state="LEFT"
					self.curpic=self.lpic
				else:
					self.state1="LEFT"
				self.dx=-10
			if evt.key == pygame.K_s:
				if self.state==None or self.state=="UP":
					self.state="DOWN"
					self.curpic=self.downpic
				else:
					self.state1="DOWN"
				self.dy=10
			if evt.key == pygame.K_d:
				if self.state==None or self.state=="LEFT":
					self.state="RIGHT"
					self.curpic=self.rpic
				else:
					self.state1="RIGHT"
				self.dx=10
			#if evt.key == pygame.K_g:#PUNCHING
			#	if self.state==None:
			#		self.curpic=self.ppic
			#	self.state="PUNCH"
		elif evt.type == pygame.KEYUP:
			if evt.key == pygame.K_w:
				if self.state=="UP":
					self.curpic=self.uppic
					self.state=None
				if self.state1=="RIGHT" or self.state1=="LEFT":
					self.state=self.state1
					self.state1=None

					if self.state=="RIGHT": self.curpic=self.rpic
					else: self.curpic=self.lpic

				self.dy=0
			if evt.key == pygame.K_a:
				if self.state=="LEFT":
					self.curpic=self.lpic
					self.state=None
				if self.state1=="UP" or self.state1=="DOWN":
					self.state=self.state1
					self.state1=None

					if self.state=="UP": self.curpic=self.uppic
					else: self.curpic=self.downpic

				self.dx=0
			if evt.key == pygame.K_s:
				if self.state=="DOWN":
					self.curpic=self.downpic
					self.state=None
				if self.state1=="RIGHT" or self.state1=="LEFT":
					self.state=self.state1
					self.state1=None

					if self.state=="RIGHT": self.curpic=self.rpic
					else: self.curpic=self.lpic

				self.dy=0
			if evt.key == pygame.K_d:
				if self.state=="RIGHT":
					self.curpic=self.rpic
					self.state=None
				if self.state1=="UP" or self.state1=="DOWN":
					self.state=self.state1

					if self.state=="UP": self.curpic=self.uppic
					else: self.curpic=self.downpic

					self.state1=None
				self.dx=0