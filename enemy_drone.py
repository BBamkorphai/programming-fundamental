import pygame
import time
from support import import_folder


class Enemy_drone(pygame.sprite.Sprite):
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
        self.image = self.animations['fly'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        

        # enemy status
        self.status = 'death'
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
        character_path = 'D:/survive! if you can/graphics/enemy_2/'
        self.animations = {'fly':[],'death':[],'permanent_death':[],'attack':[]}

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

    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        #convert vector to distance
        distance = (player_vec - enemy_vec).magnitude() 
        #print(distance)
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        #print(direction)

        return (distance, direction)

    def get_enemy_status(self,player_pos,player,UI):
        direction = self.get_player_distance_direction(player)[1]
        #print(direction)
        direction_x = direction[0]
        direction_y = direction[1]
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.direction.y >= 1000:
            self.status = 'permanent_death'
            #print("one of the enemy out of frame")
        if player.rect.colliderect(self.rect) and self.status != 'permanent_death' and self.status != 'death':
            if self.direction.x < 0 and player.direction.x <= 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.status = 'attack'
                self.on_left = True
                self.facing_right = True
                self.current_x = self.rect.left
                
                
            elif self.direction.x > 0 and player.direction.x < 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.status = 'attack'
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                
                
            elif self.direction.x > 0 and player.direction.x >= 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.status = 'attack'
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                
            elif self.direction.x < 0 and player.direction.x > 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.status = 'attack'
                self.on_right = True
                self.facing_right = True
                self.current_x = self.rect.right


        elif self.enemy_health <= 0 and self.status != 'permanent_death' and self.status != 'death':
                self.direction.x = 0
                self.direction.y = 0
                self.status = 'death'
                UI.get_score(1000)
                
                self.current_time = time.time()
                #print("death")

        elif self.enemy_damaged > 0  and self.status != 'permanent_death' and self.status != 'death' :
            self.enemy_damaged = 0
            #print("hurt")

        elif self.status != 'permanent_death' and self.status != 'death':
            #print(direction_y)
            #0.007
            #-0.007
            if direction_x >= 0:
                self.direction.x = 0.5
                self.status = 'fly'
                self.facing_right = True
            elif direction_x < -0:
                self.direction.x = -0.5
                self.status = 'fly'
                self.facing_right = False
            else:
                self.direction.x = 0
                self.status = 'fly'

            if direction_y >= 0:
                self.direction.y = 0.5
                self.status = 'fly'
            elif direction_y < 0:
                self.direction.y = -0.5
                self.status = 'fly'
            else:
                self.direction.y = 0
                self.status = 'fly'


        #distance = self.get_player_distance_direction(player)[0]

        #if distance <= self.attack_radius and self.can_attack:
            #if self.status != 'attack':
                #self.frame_index = 0
            #self.status = 'attack'
        #elif distance <= self.notice_radius:
            #self.status = 'move'
        #else:
            #self.status = 'idle'

        if time.time() - self.current_time >= self.delay_death and self.status == 'death':
            self.status = 'permanent_death'
            #print("permanent_death")
            self.current_time = time.time()
        
        

    #def enemy_killed(self,score):
        #if self.status == 'Death':
            #score += 500
        
    def spawn_shift(self,x_shift):
        self.rect.x += x_shift

    def respawn(self,pos,x_shift):
        self.direction = pygame.math.Vector2(0,0)
        self.set_rect_position(pos)
        #self.spawn_shift(x_shift)
        self.enemy_health = 50
        self.status = 'fly'
        self.enemy_damaged = 0
        #print("respawn")
        

    def update(self,x_shift, player_pos,player,UI):
        #print("str rect.x = " + str(self.rect.x))
        #print("str rect.y = " + str(self.rect.y))

        self.rect.x += x_shift
        self.get_enemy_status(player_pos,player,UI)
        self.animate()
        # print(self.status)
        #print("str direction.y = " + str(self.direction.y))
        