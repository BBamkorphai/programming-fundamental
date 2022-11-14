import pygame
import time
from support import import_folder
screen = pygame.display.set_mode((800,800))

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,create_jump_particles):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.20
        self.image = self.animations['idel'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # player_pos
        self.player_pos = pos

        #health bar
        self.current_health = 1000
        self.target_health = 1000
        self.max_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5
        
        # dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.20
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -14

        # player status
        self.status = 'idel'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # time
        self.current_time = 0
        self.last_shoot = 0
        self.shoot_delay = 0.25


    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health = self.max_health

    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0),(10,10,self.target_health / self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4)

    def advanced_health(self):
        transition_width = 0
        transition_color = (255,0,0)

        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed 
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)


        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color = (0,255,0)


        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(10,45,health_bar_width,25)
        transition_bar = pygame.Rect(health_bar.right,45,transition_width,25)
		
        pygame.draw.rect(screen,(255,0,0),health_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)	
        pygame.draw.rect(screen,(255,255,255),(10,45,self.health_bar_length,25),4)	


    def import_character_assets(self):
        character_path = 'D:\\platfrom testing\\graphics\\character\\'
        self.animations = {'idel':[],'walk':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('D:\\platfrom testing\\graphics\\character\\dust_particles\\run')

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

    def run_dust_animation(self):
        if self.status == 'walk' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6,10)
                self.display_surface.blit(dust_particle,pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6,10)
                flipped_dust_particle = pygame.transform.flip(dust_particle,True,False)
                self.display_surface.blit(flipped_dust_particle,pos)
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.jump()
            self.create_jump_particles(self.rect.midbottom)
        if keys[pygame.K_h]:
            self.get_health(200)
        if keys[pygame.K_d]:
            self.get_damage(200)

    def firer(self):
        keys_pre = pygame.key.get_pressed()
        if keys_pre[pygame.K_SPACE] and time.time() - self.current_time >= self.shoot_delay:
            self.current_time = time.time()
            # print("pressed")
            # bullet.active = True
            # ยิงกระสุน
            return True
        #keys_post = pygame.KEYUP
        #if keys_post[pygame.K_SPACE]:
            #return False
        return False

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0 and self.on_ground:
                self.status = 'walk'
            elif self.on_ground:
                self.status = 'idel'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()
        self.advanced_health()

