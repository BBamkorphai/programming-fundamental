import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,surface):
        super().__init__()

        self.display_surface = surface
      
        self.speed = 8

        self.player_pos = pos

        self.bullet_pos = self.player_pos

        self.bullet_direction = pygame.math.Vector2(0,0)
        
        self.facing_right = True

        self.image = pygame.image.load("D:\\survive! if you can\\graphics\\bullet\\5.png")
        self.rect = self.image.get_rect(topleft = pos)

        self.active = False



    #create sprite groups
    

    
    def bullet_shooted(self,bullet_pos):
        pygame.Surface.blit(self.image,self.player_pos)
        

    def set_rect_position(self,pos):
        self.rect = self.image.get_rect(topleft = pos)
        #print("set rect bullet pass")
        
    
    def bullet_move(self):
        #print("bullet move pass")
        if self.facing_right == True:
            self.bullet_direction.x = 1
        else:
            self.bullet_direction.x = -1
        self.rect.x += self.bullet_direction.x * self.speed



    def update(self,x_shift):
        #print("pass")
        self.bullet_move()
        self.rect.x += x_shift