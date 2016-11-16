import pygame
from PIL import Image
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
		self.uppic=2
		self.downpic=1
		self.rpic=3
		self.lpic=4
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