import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from player import Player
#from UI import *
from bullet import *
from button import Button
from UI_interface import UI_class
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

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('D:/survive! if you can/graphics/UI/font.ttf', size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        
        BG = pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\Background.png').convert_alpha()
        BG = pygame. transform. scale(BG, (1800, 800))
        screen.blit(BG, (0,0))
        check = True
        level.run(check)

        PLAY_BACK = Button(image=None, pos=(600, 55), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        #ui.UI_RUN()
        pygame.display.update()
        clock.tick(60)

def score_borad():
    while True:
        score_borad_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        score_borad_TEXT = get_font(45).render("This is the score_borad screen.", True, "Black")
        score_borad_RECT = score_borad_TEXT.get_rect(center=(640, 260))
        screen.blit(score_borad_TEXT, score_borad_RECT)

        score_borad_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        score_borad_BACK.changeColor(score_borad_MOUSE_POS)
        score_borad_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if score_borad_BACK.checkForInput(score_borad_MOUSE_POS):
                    main_menu()

        pygame.display.update()  

def main_menu():
    while True:
        screen.blit(BG_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        TEXT_BG = pygame.image.load('D:/survive! if you can/graphics/UI/Options Rect.png')

        MENU_TEXT = get_font(75).render("Survive!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        MENU_TEXT_2 = get_font(25).render("if you can", True, "#8B0000")
        MENU_RECT_2 = MENU_TEXT_2.get_rect(center=(640, 150))

        PLAY_BUTTON = Button(image=pygame.image.load('D:/survive! if you can/graphics/UI/Play Rect.png'), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        score_borad_BUTTON = Button(image=pygame.image.load('D:/survive! if you can/graphics/UI/Options Rect.png'), pos=(640, 400), 
                            text_input="score", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load('D:/survive! if you can/graphics/UI/Quit Rect.png'), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(MENU_TEXT_2, MENU_RECT_2)
        screen.blit(TEXT_BG, (330, 60))

        for button in [PLAY_BUTTON, score_borad_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if score_borad_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score_borad()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()