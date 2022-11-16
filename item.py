import pygame
import time
from support import import_folder


class Item(pygame.sprite.Sprite):
    def __init__(self,pos,surface): 
        super().__init__()
        # level setup
        self.display_surface = surface

        # enemy_pos
        self.enemy_pos = pos

        # enemy_health
        self.enemy_health = 0

        # decrease HP
        self.enemy_damaged = 0

        # enemy movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -14
        
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.2
        self.image = self.animations['heal_done'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        

        # enemy status
        self.status = 'heal_done'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.current_x = 0
        self.delay_death = 0.20
        self.current_time = 0
        self.hitted_time = 0
        self.delay_hit = 0.35
        self.got_time = True

    def set_rect_position(self,pos):
        self.rect = self.image.get_rect(topleft = pos)
        

    def import_character_assets(self):
        character_path = 'D:/survive! if you can/graphics/heal/'
        self.animations = {'heal':[],'heal_done':[]}

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

    def get_heal(self,player_pos,player,UI):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.direction.y >= 1000 and self.status != 'heal_done':
            self.status = 'heal_done'
            #print("one of the enemy out of frame")
        if player.rect.colliderect(self.rect) and self.status != 'heal_done':
            player.get_health(400)
            self.status = 'heal_done'   
            self.current_time = time.time()
      
    def spawn_shift(self,x_shift):
        self.rect.x += x_shift

    def respawn(self,pos,x_shift):
        self.direction = pygame.math.Vector2(0,0)
        self.set_rect_position(pos)
        self.status = 'heal'
        
    def update(self,x_shift, player_pos,player,UI):
        self.rect.x += x_shift
        self.get_heal(player_pos,player,UI)
        self.animate()