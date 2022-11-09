import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,surface,player_direction_x):
        super().__init__()
        # level setup
        self.display_surface = surface

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = player_direction_x
        self.speed = 8
        

        self.image = pygame.image.load("D:\\platfrom testing\\graphics\\bullet\\10.png")
        self.rect = self.image.get_rect(topleft = pos)


    def bullet_shooted(self):
        pass
    
    def bullet_move(self):
        pass

    def bullet_coli(self):
        pass

    def delete_bullet(self):
        pass

    def update(self):
        pygame.Surface.blit(self.image,pos)
        pass

        

