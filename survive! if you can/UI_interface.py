import pygame

class UI_class(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()

        # setup
        self.display_surface = surface

        pos = (10,85)

        # ammo image
        self.image = pygame.image.load('D:\\survive! if you can\\graphics\\UI\\item\\blank.png')

        self.rect = self.image.get_rect(topleft = pos)


        #amm0 position
        self.UI_ammo_pos = (10,85)

        # shoot
        self.number_of_shoot = 10

        # font
        self.over_font = pygame.font.Font('freesansbold.ttf', 32)

        # ammo shoot pos
        self.ammo_shoot_pos = (100,105)

        # score
        self.score = 5000

        # score_pos
        self.score_pos = (1000,55)

        

    def get_score(self,amount):
        #print("get score")
        #print(amount)
        self.score += amount
        #print(self.score)

    def show_ammo(self):
        self.display_surface.blit(self.image,self.UI_ammo_pos)
        #print("show ammo work!")

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


    def update(self):
        #print("UI update")
        self.show_ammo()
        #self.show_num_shot()
        self.show_score()
