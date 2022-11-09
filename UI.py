import pygame

class UI:
    def __init__(self,surface):

        # setup
        self.display_surface = surface

        # ammo image
        self.ammo = pygame.image.load('D:\\platfrom testing\\graphics\\UI\\item\\ammo.png')

        #amm0 position
        self.UI_ammo_pos = (10,85)

        # shoot
        self.number_of_shoot = 100

        # font
        self.over_font = pygame.font.Font('freesansbold.ttf', 32)

        # ammo shoot pos
        self.ammo_shoot_pos = (100,105)

        # score
        self.score = 0

        # score_pos
        self.score_pos = (1100,55)

    def show_ammo(self):
        self.display_surface.blit(self.ammo,self.UI_ammo_pos)

    def show_num_shot(self):
        text_surface = self.over_font.render(str(self.number_of_shoot), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.ammo_shoot_pos
        self.display_surface.blit(text_surface, text_rect)

    def show_score(self):
        text_surface = self.over_font.render('score:' + str(self.score), True, (0, 150, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.score_pos
        self.display_surface.blit(text_surface, text_rect)


    def UI_RUN(self):
        self.show_ammo()
        self.show_num_shot()
        self.show_score()
    