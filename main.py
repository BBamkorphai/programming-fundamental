import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from player import Player
from UI import *
from bullet import *
#py gmae set up
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
ui = UI_class (screen)
pygame.display.set_caption('...')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    
            sys.exit()
        
    BG = pygame.image.load('D:\\platfrom testing\\graphics\\sprite\\Background.png').convert_alpha()
    BG = pygame. transform. scale(BG, (1800, 800))
    screen.blit(BG, (0,0))
    level.run()
    ui.UI_RUN()
    pygame.display.update()
    clock.tick(60)  