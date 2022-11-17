import pygame
import time
from support import import_folder


class Enemy(pygame.sprite.Sprite):
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
        self.image = self.animations['Walk'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        

        # enemy status
        self.status = 'Death'
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

        # SFX
        self.SFX_enemy_death = pygame.mixer.Sound('D:/survive! if you can/SFX and music/enemy1_death.wav')
        self.SFX_player_hitted = pygame.mixer.Sound('D:/survive! if you can/SFX and music/player_hitted.wav')
        self.SFX_wood_attack = pygame.mixer.Sound('D:/survive! if you can/SFX and music/wood_attack.wav')

    def set_rect_position(self,pos):
        self.rect = self.image.get_rect(topleft = pos)
        

    def import_character_assets(self):
        character_path = 'D:\\survive! if you can\\graphics\\enemy_1\\'
        self.animations = {'Attack':[],'Death':[],'Hurt':[],'Walk':[],'permanant_death':[]}

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


    def get_enemy_status(self,player_pos,player,UI):
        self.rect.x += self.direction.x * self.speed
        if self.direction.y >= 1000:
            self.status = 'permanant_death'
            #print("enemy out of frame")
        if player.rect.colliderect(self.rect) and self.status != 'permanant_death' and self.status != 'Death':
            if self.direction.x < 0 and player.direction.x <= 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.SFX_wood_attack.play()
                    self.SFX_player_hitted.play()
                    self.status = 'Attack'
                self.on_left = True
                self.facing_right = True
                self.current_x = self.rect.left
                
                
            elif self.direction.x > 0 and player.direction.x < 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.SFX_player_hitted.play()
                    self.SFX_wood_attack.play()
                    self.status = 'Attack'
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                
                
            elif self.direction.x > 0 and player.direction.x >= 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.SFX_player_hitted.play()
                    self.SFX_wood_attack.play()
                    self.status = 'Attack'
                self.on_right = True
                self.facing_right = False
                self.current_x = self.rect.right
                
            elif self.direction.x < 0 and player.direction.x > 0 :
                if time.time() - self.hitted_time >= self.delay_hit:
                    self.hitted_time = time.time()
                    player.get_damage(200)
                    self.SFX_player_hitted.play()
                    self.SFX_wood_attack.play()
                    self.status = 'Attack'
                self.on_right = True
                self.facing_right = True
                self.current_x = self.rect.right


        elif self.enemy_health <= 0 and self.status != 'permanant_death' and self.status != 'Death':
                self.direction.x = 0
                self.direction.y = 0
                self.status = 'Death'
                self.SFX_enemy_death.play()
                UI.get_score(500)
                self.current_time = time.time()
                #print("death")
                

        elif self.enemy_damaged > 0  and self.status != 'permanant_death' and self.status != 'Death' :
            self.status = 'Hurt'
            self.enemy_damaged = 0
            #print("hurt")

        elif self.status != 'permanant_death' and self.status != 'Death':
            if self.facing_right == False:
                self.status = 'Walk'
                self.direction.x = -0.5
            else:
                self.status = 'Walk'
                self.direction.x = 0.5

        if time.time() - self.current_time >= self.delay_death and self.status == 'Death':
            self.status = 'permanant_death'
            #print("permanant_death")
            self.current_time = time.time()
        
        # ตายห่าตลอดกาล ๒ # แก้ได้แล้วหว่ะครับ

    #def enemy_killed(self,score):
        #if self.status == 'Death':
            #score += 500

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def spawn_shift(self,x_shift):
        self.rect.x += x_shift

    def respawn(self,pos,x_shift):
        self.direction = pygame.math.Vector2(0,0)
        self.set_rect_position(pos)
        #self.spawn_shift(x_shift)
        self.enemy_health = 100
        self.status = 'Walk'
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
        