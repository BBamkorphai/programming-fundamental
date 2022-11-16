import pygame
import time
import random
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from player import Player
from particles import ParticleEffect
from enemy import Enemy
from enemy_drone import Enemy_drone
from bullet import Bullet
from UI_interface import UI_class
from item import Item
screen = pygame.display.set_mode((screen_width,screen_height))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('D:/survive! if you can/graphics/UI/font.ttf', size)
class Level:
    def __init__(self,level_data,surface): 

        self.start_time = time.time()
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.ui_setup()
        self.world_shift_x = 0
        self.current_x = 0

        self.level_deta = level_data

        # dust 
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

        # spanwing
        self.delay_spawn = 4
        self.lasttime_spawn = time.time()

        self.total_shift = 0
        self.last_spawn = 0

        # drone spawn
        self.drone_last_spawn = 0
        self.drone_lasttime_spawn = time.time()
        self.drone_delay_spawn = 8

        # heal spawn
        self.heal_last_spawn = 0
        self.heal_lasttime_spawn = time.time()
        self.heal_delay_spawn = 60

        self.death_check = False
        self.death_time = 0
        self.setup_bullet() 

    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # particle set

    def create_jump_particles(self,pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10,5)
        else:
            pos += pygame.math.Vector2(10,-5)
        jump_particle_sprite = ParticleEffect(pos,'jump')
        self.dust_sprite.add(jump_particle_sprite)
    
    def ui_setup(self):
        self.UI_interface = pygame.sprite.GroupSingle()
        ui = UI_class(self.display_surface)
        self.UI_interface.add(ui)
    
    
    
    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10,15)
            else:
                offset = pygame.math.Vector2(-10,15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
            self.dust_sprite.add(fall_dust_particle)

    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # map set
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        self.enemy_drone = pygame.sprite.Group()
        self.item = pygame.sprite.Group()
        #self.UI_interface = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'G':                 
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'X':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\wall.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'Z':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\IndustrialTile_18.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'Q':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\mid_plate_1.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'A':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\plate_1.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'B':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\plate_2.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'C':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\plate_3.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'M':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\mid_plate_2.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'S':                
                    tile = Tile((x,y),tile_size)
                    tile.image =  pygame.image.load('D:\\survive! if you can\\graphics\\sprite\\IndustrialTile_37.png').convert_alpha()
                    self.tiles.add(tile)
                if cell == 'P':                 
                    player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
                    self.player.add(player_sprite)
                if cell == 'E':                 
                    enemy_sprite = Enemy((9000,0),self.display_surface)
                    self.enemy.add(enemy_sprite)
                    #print(str((x,y)))
                if cell == 'D':                 
                    enemy_drone_sprite = Enemy_drone((10000,0),self.display_surface)
                    self.enemy_drone.add(enemy_drone_sprite)
                    #print(str((x,y)))
                if cell == 'H':                 
                    heal_sprite = Item((10000,0),self.display_surface)
                    self.item.add(heal_sprite)

    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # bullet set
    def setup_bullet(self):
        self.bullets = pygame.sprite.Group()
        for ammo in range(0, 100):
            bullet = Bullet((9000,9000),self.display_surface)
            self.bullets.add(bullet)

    def shoot_bullet(self):
        player = self.player.sprite
        player_pos = (player.rect.x + 5, player.rect.y + 22)
        if player.firer():
            #print("returned")    
            for bullet in self.bullets.sprites():
                if bullet.active == False:
                    bullet.active = True
                    bullet.facing_right = player.facing_right
                    bullet.set_rect_position(player_pos)
                    return
    
    def bullet_horizontal_movement_collision_with_enemy(self):
        enemy_sprite = self.enemy.sprites()
        enemy_drone_sprite = self.enemy_drone.sprites()
        bullets = self.bullets.sprites()

        for sprite_enemy in enemy_sprite:
            for bullet in self.bullets.sprites():
                if bullet.rect.colliderect(sprite_enemy.rect) and sprite_enemy.status != 'permanant_death' and sprite_enemy.status != 'death':
                    sprite_enemy.enemy_damaged += 25
                    sprite_enemy.enemy_health -= 25
                    bullet.set_rect_position((9000,9000))
                    bullet.active = False
                    #if sprite_enemy.on_left and (sprite_enemy.rect.left < self.current_x or sprite_enemy.direction.x >= 0):
                        #sprite_enemy.on_left = False
                    #if sprite_enemy.on_right and (sprite_enemy.rect.right > self.current_x or sprite_enemy.direction.x <= 0):
                        #sprite_enemy.on_right = False
        for sprite_enemy_drone in enemy_drone_sprite:
            for bullet in self.bullets.sprites():
                if bullet.rect.colliderect(sprite_enemy_drone.rect) and sprite_enemy_drone.status != 'permanent_death' and sprite_enemy_drone.status != 'death':
                    sprite_enemy_drone.enemy_damaged += 25
                    sprite_enemy_drone.enemy_health -= 25
                    bullet.set_rect_position((9000,9000))
                    bullet.active = False

    def bullet_horizontal_movement_collision_with_tiles(self):
        bullets = self.bullets.sprites()

        for sprite_tile in self.tiles.sprites():
            for bullet in self.bullets.sprites():
                if bullet.rect.colliderect(sprite_tile.rect):
                    bullet.set_rect_position((9000,9000))
                    bullet.active = False

        
    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # world shift set
    def scroll_x(self):
        player = self.player.sprite
        #enemy = self.enemy.sprite
        enemy = self.enemy.sprites()
        enemy_drone = self.enemy_drone.sprites()
        heal_box = self.item.sprites()
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift_x = 6
            player.speed = 0
            
            
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift_x = -6
            player.speed = 0
            
        else:
            self.world_shift_x = 0
            player.speed = 4
            

        for sprite_enemy in enemy:
            if player_x < screen_width / 4 and direction_x < 0:
                self.world_shift_x = 6
                sprite_enemy.speed = 4
            
            elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
                self.world_shift_x = -6
                sprite_enemy.speed = 4
            else:
                self.world_shift_x = 0
                sprite_enemy.speed = 4

        for sprite_enemy_drone in enemy_drone:
            if player_x < screen_width / 4 and direction_x < 0:
                self.world_shift_x = 6
                sprite_enemy_drone.speed = 4
            
            elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
                self.world_shift_x = -6
                sprite_enemy_drone.speed = 4
            else:
                self.world_shift_x = 0
                sprite_enemy_drone.speed = 4

        for heal_move in heal_box:
            if player_x < screen_width / 4 and direction_x < 0:
                self.world_shift_x = 6
                heal_move.speed = 4
            
            elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
                self.world_shift_x = -6
                heal_move.speed = 4
            else:
                self.world_shift_x = 0
                heal_move.speed = 4

    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # player colision set

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False
 
    # ++ + + + + + + + + + + ++ + + + + + + +  ++ + + + + + +  ++ + + + +  + ++  +
    # enemy colision set
    def enemy_horizontal_movement_collision(self):
        #enemy = self.enemy.sprite
        enemy = self.enemy.sprites()
        #enemy.rect.x += enemy.direction.x * enemy.speed

        for sprite_enemy in enemy:
            sprite_enemy.rect.x += sprite_enemy.direction.x * sprite_enemy.speed
            for sprite_tile in self.tiles.sprites():
                
                if sprite_tile.rect.colliderect(sprite_enemy.rect):
                    if sprite_enemy.direction.x < 0:
                        sprite_enemy.rect.left = sprite_tile.rect.right
                        sprite_enemy.facing_right = True
                        sprite_enemy.on_left = True
                        self.current_x = sprite_enemy.rect.left
                    elif sprite_enemy.direction.x > 0:
                        sprite_enemy.rect.right = sprite_tile.rect.left
                        sprite_enemy.facing_right = False
                        sprite_enemy.on_right = True
                        self.current_x = sprite_enemy.rect.right

                    if sprite_enemy.on_left and (sprite_enemy.rect.left < self.current_x or sprite_enemy.direction.x >= 0):
                        sprite_enemy.on_left = False
                    if sprite_enemy.on_right and (sprite_enemy.rect.right > self.current_x or sprite_enemy.direction.x <= 0):
                        sprite_enemy.on_right = False

    def enemy_vertical_movement_collision(self):
        #enemy = self.enemy.sprite
        enemy = self.enemy.sprites()

        for sprite_enemy in enemy:
            sprite_enemy.apply_gravity()
            for sprite_tile in self.tiles.sprites():
                
                if sprite_tile.rect.colliderect(sprite_enemy.rect):
                    if sprite_enemy.direction.y > 0:
                        sprite_enemy.rect.bottom = sprite_tile.rect.top
                        sprite_enemy.direction.y = 0
                        sprite_enemy.on_ground = True
                    elif sprite_enemy.direction.y < 0:
                        sprite_enemy.rect.top = sprite_tile.rect.bottom
                        sprite_enemy.direction.y = 0
                        sprite_enemy.on_ceiling = True

                    if sprite_enemy.on_left and (sprite_enemy.rect.left < self.current_x or sprite_enemy.direction.x >= 0):
                        sprite_enemy.on_left = False
                    if sprite_enemy.on_right and (sprite_enemy.rect.right > self.current_x or sprite_enemy.direction.x <= 0):
                        sprite_enemy.on_right = False

                    if sprite_enemy.on_ground and sprite_enemy.direction.y < 0 or sprite_enemy.direction.y > 1:
                        sprite_enemy.on_ground = False
                    if sprite_enemy.on_ceiling and sprite_enemy.direction.y > 0.1:
                        sprite_enemy.on_ceiling = False


    def spawn_enemy(self,x_shift):
        spawn_point = random.randint(1,6)
        spawn_point_number = 0
        if spawn_point == self.last_spawn:
            spawn_point += 1
        for row_index,row in enumerate(self.level_deta):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'E':
                    spawn_point_number += 1
                    if spawn_point_number == spawn_point:
                        self.last_spawn = spawn_point
                        for enemy in self.enemy.sprites():
                            if enemy.status == 'permanant_death':
                                enemy.respawn((x+self.total_shift,y),x_shift)
                                #print(str((x,y)))
                                return

    def spawn_enemy_drone(self,x_shift):
        spawn_point = random.randint(1,6)
        spawn_point_number = 0
        if spawn_point == self.drone_last_spawn:
            spawn_point += 1
        for row_index,row in enumerate(self.level_deta):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'D':
                    spawn_point_number += 1
                    if spawn_point_number == spawn_point:
                        self.drone_last_spawn = spawn_point
                        for enemy_drone in self.enemy_drone.sprites():
                            if enemy_drone.status == 'permanent_death':
                                enemy_drone.respawn((x+self.total_shift,y),x_shift)
                                #print("respawn")
                                #print(str((x,y)))
                                return
    
    
    def spawn_heal(self,x_shift):
        spawn_point = random.randint(1,3)
        spawn_point_number = 0
        if spawn_point ==  self.heal_last_spawn:
            spawn_point += 1
        for row_index,row in enumerate(self.level_deta):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'H':
                    spawn_point_number += 1
                    if spawn_point_number == spawn_point:
                        self.heal_last_spawn = spawn_point
                        for heal_box in self.item.sprites():
                            if heal_box.status == 'heal_done':
                                heal_box.respawn((x+self.total_shift,y),x_shift)
                                #print("respawn")
                                #print(str((x,y)))
                                return
                            
        
    def run(self,check):
        if check == True:
            self.total_shift += self.world_shift_x
            # print("total.shift = " + str(self.total_shift))
            # dust particles 
            self.dust_sprite.update(self.world_shift_x)
            self.dust_sprite.draw(self.display_surface)

            # level tiles
            self.tiles.update(self.world_shift_x)
            self.tiles.draw(self.display_surface)
            self.scroll_x()

        
            # player
            #   self.player.update()
            self.horizontal_movement_collision()
            self.get_player_on_ground()
            self.vertical_movement_collision()
        
            self.player.update()
            self.create_landing_dust()
            self.player.draw(self.display_surface)

            #    enemy1
            player = self.player.sprite
            ui = self.UI_interface.sprite
            score = ui.score
            player_pos = (player.rect.x, player.rect.y)
            if time.time() - self.lasttime_spawn >= self.delay_spawn:
                #print("enemy spawned")
                self.spawn_enemy(self.world_shift_x)
                #print("spawn")
                self.lasttime_spawn = time.time()
            self.enemy.update(self.world_shift_x,player_pos,player,ui)
            self.enemy_horizontal_movement_collision()
            self.enemy_vertical_movement_collision()
            self.enemy.draw(self.display_surface)
            #print("time.time() is ")
            #print(time.time())
            #enemy drone
            if time.time() - self.start_time >= 60:
                if time.time() - self.drone_lasttime_spawn >= self.drone_delay_spawn:
                    #print("enemy spawned")
                    self.spawn_enemy_drone(self.world_shift_x)
                    self.drone_lasttime_spawn = time.time()
                if time.time() - self.start_time >= 120:
                    self.drone_delay_spawn = 4
                    #print(self.drone_delay_spawn)
            self.enemy_drone.update(self.world_shift_x,player_pos,player,ui)
            self.enemy_drone.draw(self.display_surface)
        

            # bullet
            self.shoot_bullet()
            self.bullets.update(self.world_shift_x)
            self.bullets.draw(self.display_surface)
            self.bullet_horizontal_movement_collision_with_enemy()
            self.bullet_horizontal_movement_collision_with_tiles()

            # heal_box
            if time.time() - self.start_time >= 60:
                if time.time() - self.heal_lasttime_spawn >= self.heal_delay_spawn:
                    #print("enemy spawned")
                    self.spawn_heal(self.world_shift_x)
                    self.heal_lasttime_spawn = time.time()
                    #print(self.drone_delay_spawn)
            self.item.update(self.world_shift_x,player_pos,player,ui)
            self.item.draw(self.display_surface)

            # UI

            self.UI_interface.update()
            self.UI_interface.draw(self.display_surface)

            if player.status == 'death' and self.death_check == False:
                self.death_time = time.time()
                self.death_check = True

            delay_death_time = 0.4

            if player.status == 'death' and time.time() - self.death_time >= delay_death_time:
                screen.fill("black")
                TEXT_AFTER_DEATH = get_font(25).render("you didn't make it", True, "#b68f40")
                TEXT_AFTER_DEATH_RECT = TEXT_AFTER_DEATH.get_rect(center=(600, 100))
                screen.blit(TEXT_AFTER_DEATH, TEXT_AFTER_DEATH_RECT)

                TEXT_AFTER_SCORE_DEATH = get_font(25).render("your score is", True, "#b68f40")
                TEXT_AFTER_DEATH_SCORE_RECT = TEXT_AFTER_DEATH.get_rect(center=(640, 200))
                screen.blit(TEXT_AFTER_SCORE_DEATH, TEXT_AFTER_DEATH_SCORE_RECT)

                SCORE_AFTER_DEATH = get_font(75).render(str(score), True, "#b68f40")
                SCORE_RECT = SCORE_AFTER_DEATH.get_rect(center=(600, 368))
                screen.blit(SCORE_AFTER_DEATH, SCORE_RECT)
                #check = False


        
        
        

