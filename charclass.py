import pygame
from PIL import Image
import random

class Map:
	def __init__(self):
		self.nooftrees=random.randint(10,15)
		self.treelocs=[]
		self.imgs=[None]*400
		for i in range(self.nooftrees):
			self.treelocs.append((random.randint(0,20),random.randint(0,20)))
		self.initmap()
	def checkcollision(self,(x,y)):
		x=x/50
		y=y/50
		if (x,y) in treelocs:
			return True
		return False
	def loadimg(self,file):
		image=pygame.image.load(file).convert()
		return image
	def initmap(self):
		x=0
		for i in range(20):
			for j in range(20):
				if (i,j) in self.treelocs:
					self.imgs[x]=self.loadimg("Images/tree.png")
				else:
					self.imgs[x]=self.loadimg("Images/ground.png")
				x+=1
	def blitmap(self,wind):
		i=0
		j=0
		x=0
		while i<1000:
			while j<1000:
				wind.blit(self.imgs[x],[i,j])
				x+=1
				j+=50
			i+=50
			j=0
class Goku:
	def getImgLib(self,file):
		lib=[]
		for i in range(196):
			lib.append(pygame.image.load("Images/Goku"+str(i)+".png").convert_alpha())
		return lib


	def __init__(self,window,x,y):
		self.image_lib=self.getImgLib("Goku.png")
		self.state=None
		self.X=x
		self.Y=y
		self.dx=0
		self.dy=0
		self.curpic=1
		self.nextpic=""
		self.uppic=2
		self.downpic=1
		self.rpic=3
		self.lpic=4
		self.ppic=0
		self.window=window
		self.window.blit(self.image_lib[1],(x,y))


	def update(self):
		self.window.blit(self.image_lib[self.curpic],(self.X,self.Y))


	def Move(self,evt):
		if evt.type == pygame.KEYDOWN:
			if evt.key == pygame.K_w:
				if self.state=="UP":
					self.curpic+=4
					if self.curpic>40:
						self.curpic=self.uppic
				if self.state==None or self.state=="DOWN":
					self.state="UP"
					self.curpic=self.uppic
				self.dy=-10
			if evt.key == pygame.K_a:
				if self.state=="LEFT":
					self.curpic+=4
					if self.curpic>40:
						self.curpic=self.lpic
				if self.state==None or self.state=="RIGHT":
					self.state="LEFT"
					self.curpic=self.lpic
				self.dx=-10
			if evt.key == pygame.K_s:
				if self.state=="DOWN":
					self.curpic+=4
					if self.curpic>40:
						self.curpic=self.downpic
				if self.state==None or self.state=="UP":
					self.state="DOWN"
					self.curpic=self.downpic
				self.dy=10
			if evt.key == pygame.K_d:
				if self.state=="RIGHT":
					self.curpic+=4
					if self.curpic>40:
						self.curpic=self.rpic
				if self.state==None or self.state=="LEFT":
					self.state="RIGHT"
					self.curpic=self.rpic
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
				self.dy=0
			if evt.key == pygame.K_a:
				if self.state=="LEFT":
					self.curpic=self.lpic
					self.state=None
				self.dx=0
			if evt.key == pygame.K_s:
				if self.state=="DOWN":
					self.curpic=self.downpic
					self.state=None
				self.dy=0
			if evt.key == pygame.K_d:
				if self.state=="RIGHT":
					self.curpic=self.rpic
					self.state=None
				self.dx=0