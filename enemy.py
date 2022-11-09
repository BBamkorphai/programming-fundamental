import pygame
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,surface): 
        super().__init__()
        # level setup
        self.display_surface = surface

        # enemy_pos
        self.enemy_pos = pos

        # enemy_health
        self.enemy_health = 100

        # decrease HP
        self.enemy_damaged = 0

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -14
        
        self.import_character_assets()
        print(len(self.animations['Walk']))
        self.frame_index = 0
        self.animation_speed = 0.20
        self.image = self.animations['Walk'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        

        # player status
        self.status = 'Walk'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.current_x = 0

    def import_character_assets(self):
        character_path = 'D:\\platfrom testing\\graphics\\enemy_1\\'
        self.animations = {'Attack':[],'Death':[],'Hurt':[],'Walk':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over forframe index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0 

        image = animation[int(self.frame_index)]   
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)


    def get_enemy_status(self,player_pos,player):
        self.rect.x += self.direction.x * self.speed
        if player.rect.colliderect(self.rect):
            if self.direction.x < 0 and player.direction.x <= 0 :
                self.on_left = True
                self.facing_right = True
                self.current_x = self.rect.left
                self.status = 'Attack'
                
            elif self.direction.x > 0 and player.direction.x < 0:
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                self.status = 'Attack'
                
            elif self.direction.x > 0 and player.direction.x >= 0:
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                self.status = 'Attack'
                
            elif self.direction.x < 0 and player.direction.x > 0:
                self.on_right = True
                self.facing_right = True
                self.current_x = self.rect.right
                self.status = 'Attack'
                

        elif self.enemy_health <= 0 :
            self.status = 'death'
        elif self.enemy_damaged > 0:
            self.status = 'Hurt'
        else:
            if self.facing_right == False:
                self.status = 'Walk'
                self.direction.x = -0.5
            else:
                self.status = 'Walk'
                self.direction.x = 0.5

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        

    def update(self,x_shift, player_pos,player):
        self.rect.x += x_shift
        self.get_enemy_status(player_pos,player)
        self.animate()