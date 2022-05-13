import pygame
import pygame_menu
import sys
import math
import random

class Computer(pygame.sprite.Sprite):
    def __init__(self, pos, group, image):
        super().__init__(group)
        self.og_image = pygame.transform.rotate(scale_image(pygame.image.load(image),.25).convert_alpha(), 180) #Changed
        self.mask_image = pygame.transform.rotate(scale_image(pygame.image.load(image),.05).convert_alpha(), 180) #Changed
        self.computer_mask = pygame.mask.from_surface(self.mask_image)
        self.image = self.og_image
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = random.randint(-4,4)
        while self.speed == 0:
            self.speed = random.randint(-4,4)
        self.angle = 0
        self.rotation_speed = 5
        self.rotation_direction = 0
        self.laps = 0
        self.path = 1

    def move(self):
        radians = math.radians(self.angle) # Trying to use this code, it works for the 1st path but does not for the 2nd.
        vertical = math.cos(radians)
        horizontal = math.sin(radians)

        # Have to add the movement directly to the car's rectangle for car to move 
        self.rect.centery -= vertical * self.speed
        self.rect.centerx -= horizontal * self.speed



    def rotate(self, coordinates_comp, coordinates_mask):
        comp_vect = pygame.math.Vector2(coordinates_comp[0],coordinates_comp[1]) # Puts the coordinates of the computer into a vector
        mask_vect = pygame.math.Vector2(coordinates_mask[0],coordinates_mask[1]) # Puts the coordinates of the path's mask into a vector

        self.angle = comp_vect.angle_to(mask_vect) # Gets the angle of the vectors
        self.image = pygame.transform.rotozoom(self.og_image, self.angle, 1) # Rotates the image of the car

    def update_path(self):
        self.path += 1

    def update_lap(self):
        if self.path == 18:
            self.laps += 1


    def update(self):
        self.move()

    def collide(self, mask, x=0, y=0):
        offset = (int(self.rect.centerx - x), int(self.rect.centery - y))
        computer_collide = mask.overlap(self.computer_mask, offset)
        return computer_collide

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        if group is not None:
            super().__init__(group)
            self.og_image = pygame.transform.rotate(scale_image(pygame.image.load('player.png'),.25).convert_alpha(), 180)
            self.mask_image = pygame.transform.rotate(scale_image(pygame.image.load('player.png'),.05).convert_alpha(), 180)
            self.player_mask = pygame.mask.from_surface(self.mask_image)
            self.image = self.og_image
            self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.angle = 0
        self.rotation_speed = 5
        self.rotation_direction = 0
        self.laps = 0
        self.check_points = 0

    def input(self):
        keys = pygame.key.get_pressed()

        ## TO MOVE AND DONT GO OFF SCREEN
        if keys[pygame.K_w]:
            self.direction.y = -1
        ## TO MOVE AND DONT GO OFF SCREEN
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        ## TO MOVE AND DONT GO OFF SCREEN
        if keys[pygame.K_d]:
            self.direction.x = 1
            ## TO MOVE AND DONT GO OFF SCREEN
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def rotate(self):
        ## ROTATE THE CAR
        if self.rotation_direction == 1:
            self.angle -= self.rotation_speed
        if self.rotation_direction == -1:
            self.angle += self.rotation_speed

        self.image = pygame.transform.rotozoom(self.og_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.input()
        self.rotate()
        self.rect.center += (self.direction * self.speed)

    def collide(self, mask, x=0, y=0):
        offset = (int(self.rect.centerx - x), int(self.rect.centery - y))
        player_collide = mask.overlap(self.player_mask, offset)
        return player_collide
    
    def update_lap(self):
        if self.check_points == 0 and self.laps == 0:
            self.laps += 1
            print("Lap: " + str(self.laps))
        elif self.check_points == 5 and self.laps == 1:
            self.check_points = 0
            self.laps += 1
            print("Lap: " + str(self.laps))
        elif self.check_points == 5 and self.laps == 2:
            self.check_points = 0
            self.laps += 1
            print("Lap: " + str(self.laps))
        elif self.check_points == 5 and self.laps == 3:
            self.check_points = 0
            self.laps += 1
            print("Lap: " + str(self.laps))
        elif self.check_points == 5 and self.laps == 4:
            self.check_points = 0
            self.laps += 1
            print("Lap: " + str(self.laps))
        elif self.check_points == 5 and self.laps == 5:
            self.check_points = 0
            self.laps += 1
            print("You win!")

    def update_checkpoint(self):
        self.check_points += 1
        print("Check Point: " + str(self.check_points))

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # ground
        # create all surfaces from images
        # Track and track border images
        self.ground_surf = pygame.image.load('track.png').convert()
        self.back_surf = scale_image(pygame.image.load("track_boundary.png"), 1)

        # All checkpoints for user images
        self.checkpoint_one = pygame.image.load('check_1.png')
        self.checkpoint_two = pygame.image.load('check_2.png')
        self.checkpoint_three = pygame.image.load('check_3.png')
        self.checkpoint_four = pygame.image.load('check_4.png')
        self.checkpoint_five= pygame.image.load('check_5.png')

        self.finish = pygame.image.load('finish_line.png')

        # All Path images for AI
        self.path1 =  pygame.image.load('path1.png')
        self.path2 =  pygame.image.load('path2.png')
        self.path3 =  pygame.image.load('path3.png')
        self.path4 =  pygame.image.load('path4.png')
        self.path5 =  pygame.image.load('path5.png')
        self.path6 =  pygame.image.load('path6.png')
        self.path7 =  pygame.image.load('path7.png')
        self.path8 =  pygame.image.load('path8.png')
        self.path9 =  pygame.image.load('path9.png')
        self.path10 =  pygame.image.load('path10.png')
        self.path11 =  pygame.image.load('path11.png')
        self.path12 =  pygame.image.load('path12.png')
        self.path13 =  pygame.image.load('path13.png')
        self.path14 =  pygame.image.load('path14.png')
        self.path15 =  pygame.image.load('path15.png')
        self.path16 =  pygame.image.load('path16.png')
        self.path17 =  pygame.image.load('path17.png')
        self.path18 =  pygame.image.load('path18.png')


        # self.back_rect = self.back_surf.get_rect(topleft=(0, 0))
        # self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

        # Create masks for collision purposes for player
        self.track_border_mask = pygame.mask.from_surface(self.back_surf)
        self.checkpoint_one_mask = pygame.mask.from_surface(self.checkpoint_one)
        self.checkpoint_two_mask = pygame.mask.from_surface(self.checkpoint_two)
        self.checkpoint_three_mask = pygame.mask.from_surface(self.checkpoint_three)
        self.checkpoint_four_mask = pygame.mask.from_surface(self.checkpoint_four)
        self.checkpoint_five_mask = pygame.mask.from_surface(self.checkpoint_five)

        self.finish_mask = pygame.mask.from_surface(self.finish)

        # Create all masks for the paths for the AI
        self.path1_mask = pygame.mask.from_surface(self.path1)
        self.path2_mask = pygame.mask.from_surface(self.path2)
        self.path3_mask = pygame.mask.from_surface(self.path3)
        self.path4_mask = pygame.mask.from_surface(self.path4)
        self.path5_mask = pygame.mask.from_surface(self.path5)
        self.path6_mask = pygame.mask.from_surface(self.path6)
        self.path7_mask = pygame.mask.from_surface(self.path7)
        self.path8_mask = pygame.mask.from_surface(self.path8)
        self.path9_mask = pygame.mask.from_surface(self.path9)
        self.path10_mask = pygame.mask.from_surface(self.path10)
        self.path11_mask = pygame.mask.from_surface(self.path11)
        self.path12_mask = pygame.mask.from_surface(self.path12)
        self.path13_mask = pygame.mask.from_surface(self.path13)
        self.path14_mask = pygame.mask.from_surface(self.path14)
        self.path15_mask = pygame.mask.from_surface(self.path15)
        self.path16_mask = pygame.mask.from_surface(self.path16)
        self.path17_mask = pygame.mask.from_surface(self.path17)
        self.path18_mask = pygame.mask.from_surface(self.path18)


    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)

        # Displaying The Background, Track Border, and Finish Line
        self.display_surface.blit(self.ground_surf,-self.offset)
        self.display_surface.blit(self.finish,-self.offset)
        self.display_surface.blit(self.back_surf, -self.offset)

        # ALL FOR PURPOSE OF SEEING WHERE THE PATH IS FOR THE AI
        #self.display_surface.blit(self.path1, -self.offset)
        #self.display_surface.blit(self.path2, -self.offset)
        #self.display_surface.blit(self.path3, -self.offset)
        #self.display_surface.blit(self.path4, -self.offset)
        #self.display_surface.blit(self.path5, -self.offset)
        #self.display_surface.blit(self.path6, -self.offset)
        #self.display_surface.blit(self.path7, -self.offset)
        #self.display_surface.blit(self.path8, -self.offset)
        #self.display_surface.blit(self.path9, -self.offset)
        #self.display_surface.blit(self.path10, -self.offset)
        #self.display_surface.blit(self.path11, -self.offset)
        #self.display_surface.blit(self.path12, -self.offset)
        #self.display_surface.blit(self.path13, -self.offset)
        #self.display_surface.blit(self.path14, -self.offset)
        #self.display_surface.blit(self.path15, -self.offset)
        #self.display_surface.blit(self.path16, -self.offset)
        #self.display_surface.blit(self.path17, -self.offset)
        #self.display_surface.blit(self.path18, -self.offset)



        # active elements
        # Display the cars 
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)
