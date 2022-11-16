#from turtle import position
import pygame 

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		sprite_1 = pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\ground.png').convert_alpha()
		self.image = pygame.Surface((size,size))
		self.image = sprite_1
		self.rect = self.image.get_rect(topleft = pos)

	def update(self,x_shift):
		self.rect.x += x_shift