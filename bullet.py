import pygame
from spritesheet import SpriteSheet


class Bullet:
    def __init__(self, shooter, width, height, sprite):
        self.shooter = shooter
        self.mvt_speed = 8
        self.x = shooter.positionx + shooter.crosshair_x
        self.y = shooter.positiony + shooter.crosshair_y
        self.hit_box = pygame.Rect(self.x, self.y, width, height)
        self.direction = shooter.action
        self.duration = 2000
        self.birth = pygame.time.get_ticks()

        if self.direction == 0 or self.direction == 8:
            self.mvt_x = 0
            self.mvt_y = -self.mvt_speed
        elif self.direction == 1 or self.direction == 9:
            self.mvt_x = self.mvt_speed
            self.mvt_y = -self.mvt_speed
        elif self.direction == 2 or self.direction == 10:
            self.mvt_x = self.mvt_speed
            self.mvt_y = 0
        elif self.direction == 3 or self.direction == 11:
            self.mvt_x = self.mvt_speed
            self.mvt_y = self.mvt_speed
        elif self.direction == 4 or self.direction == 12:
            self.mvt_x = 0
            self.mvt_y = self.mvt_speed
        elif self.direction == 5 or self.direction == 13:
            self.mvt_x = -self.mvt_speed
            self.mvt_y = self.mvt_speed
        elif self.direction == 6 or self.direction == 14:
            self.mvt_x = -self.mvt_speed
            self.mvt_y = 0
        elif self.direction == 7 or self.direction == 15:
            self.mvt_x = -self.mvt_speed
            self.mvt_y = -self.mvt_speed

        self.sprite_sheet_image = pygame.image.load(sprite).convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [4]
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.step_counter = 0

        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 10, 10, 4, (254, 254, 254)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

    def movement(self):
        self.x += self.mvt_x
        self.y += self.mvt_y
        self.hit_box[0] = self.x
        self.hit_box[1] = self.y

    def is_over(self):
        if pygame.time.get_ticks() - self.birth >= self.duration:
            self.shooter.has_bullet = False
            return 1
        else:
            return 0

    def update_movement(self, collision_type):
        if collision_type == 1 and self.mvt_y < 0:
            self.mvt_y *= -1
            if self.mvt_x == 0:
                self.mvt_x = self.mvt_speed
        elif collision_type == 2 and self.mvt_y > 0:
            self.mvt_y *= -1
            if self.mvt_x == 0:
                self.mvt_x = self.mvt_speed
        elif collision_type == 3 and self.mvt_x > 0:
            self.mvt_x *= -1
            if self.mvt_y == 0:
                self.mvt_y = -self.mvt_speed
        elif collision_type == 4 and self.mvt_x < 0:
            self.mvt_x *= -1
            if self.mvt_y == 0:
                self.mvt_y = -self.mvt_speed
