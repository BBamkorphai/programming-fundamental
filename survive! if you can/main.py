import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from player import Player
#from UI import *
from bullet import *
from button import Button
from UI_interface import UI_class
from scorebroad import Scorebroad
import json

#py gmae set up
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
print(screen_width)
print(screen_height)
#ui = UI_class (screen)
pygame.display.set_caption('survive! if you can')

BG_menu = pygame.image.load('D:/survive! if you can/graphics/UI/menu_background.png')

game_opening_SFX = pygame.mixer.music.load('D:/survive! if you can/SFX and music/background.wav')
pygame.mixer.music.set_volume(0.3)
#game_opening_SFX.set_volume(0.5)
pygame.mixer.music.play(-1)

surface = pygame.display.get_surface()

name = Scorebroad()

ui = UI_class(surface)



BG = pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\Background.png').convert_alpha()
BG = pygame. transform. scale(BG, (1800, 800))
TEXT_BG = pygame.image.load('D:/survive! if you can/graphics/UI/Options Rect.png')
PLAY_BUTTON_image=pygame.image.load('D:/survive! if you can/graphics/UI/Play Rect.png')
SCORE_BUTTON_image=pygame.image.load('D:/survive! if you can/graphics/UI/Options Rect.png')
QUIT_BUTTON_image=pygame.image.load('D:/survive! if you can/graphics/UI/Quit Rect.png')

scoreboard = {
	'god' : 9999999
}
try:
	with open('sc.txt') as score_file:
		scoreboard = json.load(score_file)
except: 
	pass

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('D:/survive! if you can/graphics/UI/font.ttf', size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('sc.txt', 'w') as score_file:
                    json.dump(scoreboard,score_file)
                pygame.quit()    
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        
        screen.blit(BG, (0,0))
        
        level.run()
        if level.game_end == True and level.checker_text != True:
            name.text_input(scoreboard, level)
        elif level.game_end == True and level.checker_text == True:
            main_menu()

        PLAY_BACK = Button(image=None, pos=(600, 55), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        #ui.UI_RUN()
        pygame.display.update()
        clock.tick(60)

def score_broad():
    while True:

        screen.blit(BG_menu, (0, 0))

        score_broad_MOUSE_POS = pygame.mouse.get_pos()

        score_broad_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        score_broad_BACK.changeColor(score_broad_MOUSE_POS)
        score_broad_BACK.update(screen)

        name.show_score(scoreboard)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('sc.txt', 'w') as score_file:
                    json.dump(scoreboard,score_file)                
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if score_broad_BACK.checkForInput(score_broad_MOUSE_POS):
                    main_menu()

        pygame.display.update()  

def main_menu():
    while True:
        
        
        screen.blit(BG_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        

        MENU_TEXT = get_font(75).render("Survive!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        MENU_TEXT_2 = get_font(25).render("if you can", True, "#8B0000")
        MENU_RECT_2 = MENU_TEXT_2.get_rect(center=(640, 150))

        PLAY_BUTTON = Button(PLAY_BUTTON_image, pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        score_broad_BUTTON = Button(SCORE_BUTTON_image, pos=(640, 400), 
                            text_input="score", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(QUIT_BUTTON_image, pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(MENU_TEXT_2, MENU_RECT_2)
        screen.blit(TEXT_BG, (330, 60))

        for button in [PLAY_BUTTON, score_broad_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('sc.txt', 'w') as score_file:
                    json.dump(scoreboard,score_file)                
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("fuck off this damn project")
                    level.game_end = False 
                    level.checker_text = False
                    Player.status = 'idel'
                    #pygame.mixer.fadeout()
                    
                    #Player((285,650),level.display_surface,level.create_jump_particles)
                    #Level(level_map,screen)
                    Player.current_health = 1000
                    
                    play()
                if score_broad_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score_broad()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()