import pygame
from PIL import Image
class Goku:
	def getImgLib(self,file):
		lib=[]
		for i in range(196):
			lib.append(pygame.image.load("Images/Goku"+str(i)+".png").convert_alpha())
		return lib

	def __init__(self,curdir,window,x,y):
		self.image_lib=self.getImgLib("Goku.png")
		self.curpic=1
		self.state=None
		self.X=x
		self.Y=y
		self.dx=0
		self.dy=0
		self.uppic=2
		self.downpic=1
		self.rpic=3
		self.lpic=4
		self.window=window
		self.window.blit(self.image_lib[1],(x,y))
	
	def put(self,loc):
		self.window.blit(self.image_lib[loc],(self.X,self.Y))


	def up_movement(self):
		if self.state=="UP" or self.state=="DOWN":
			if self.uppic > 40:
				self.uppic=2
			self.uppic+=4
			self.curpic=self.uppic
		return None

	def down_movement(self):
		if self.state=="UP" or self.state=="DOWN":
			if self.downpic > 40:
				self.downpic=1
			self.downpic+=4
			self.curpic=self.downpic
		return None

	def right_movement(self):
		if self.state=="RIGHT" or self.state=="LEFT":
			if self.rpic > 40:
				self.rpic=3
			self.rpic+=4
			self.curpic=self.rpic
		return None

	def left_movement(self):
		if self.state=="RIGHT" or self.state=="LEFT":
			if self.lpic > 40:
				self.lpic=4
			self.lpic+=4
			self.curpic=self.lpic
		return None

	def Move(self,evt):
		if evt.type == pygame.KEYDOWN:
			if evt.key == pygame.K_w:
				if self.state==None or self.state=="DOWN":
					self.state="UP"
				self.curdir="UP"
				self.dy=-10
				self.up_movement()
			if evt.key == pygame.K_a:
				if self.state==None or self.state=="RIGHT":
					self.state="LEFT"
				self.curdir="LEFT"
				self.dx=-10
				self.left_movement()
			if evt.key == pygame.K_s:
				if self.state==None or self.state=="UP":
					self.state="DOWN"
				self.curdir="DOWN"
				self.dy=10
				self.down_movement()
			if evt.key == pygame.K_d:
				if self.state==None or self.state=="LEFT":
					self.state="RIGHT"
				self.curdir="RIGHT"
				self.dx=10
				self.right_movement()
		elif evt.type == pygame.KEYUP:
			if evt.key == pygame.K_w:
				self.dy=0
			if evt.key == pygame.K_a:
				self.dx=0
			if evt.key == pygame.K_s:
				self.dy=0
			if evt.key == pygame.K_d:
				self.dx=0
		

