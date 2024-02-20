import pygame
from spritesheet import SpriteSheet


class Bullet:
    def __init__(self, shooter, width, height, sprite):
        self.width = width
        self.height = height
        self.shooter = shooter
        self.mvt_speed = 8
        self.telekinesis = 4
        self.hit_box = pygame.Rect(0, 0, width, height)
        self.hit_box.center = shooter.hit_box.center
        self.x = self.hit_box.topleft[0]
        self.y = self.hit_box.topleft[1]
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

    def move_x(self):
        self.x += self.mvt_x
        self.hit_box[0] = self.x

    def move_y(self):
        self.y += self.mvt_y
        self.hit_box[1] = self.y

    def update_mvt_x(self, collider):
        if self.mvt_y == 0:
            if self.mvt_x > 0:
                self.mvt_y = self.mvt_speed
            else:
                self.mvt_y = -self.mvt_speed

        if self.x < collider[0]:
            self.x = collider[0] - self.width
        else:
            self.x = collider[0] + collider[2]
        self.x -= self.mvt_x
        self.hit_box[0] = self.x
        self.mvt_x *= -1

    def update_mvt_y(self, collider):
        if self.mvt_x == 0:
            if self.mvt_y > 0:
                self.mvt_x = -self.mvt_speed
            else:
                self.mvt_x = self.mvt_speed

        if self.y < collider[1]:
            self.y = collider[1] - self.height
        else:
            self.y = collider[1] + collider[3]
        self.y -= self.mvt_y
        self.hit_box[1] = self.y
        self.mvt_y *= -1
        if self.mvt_x == 0:
            if self.mvt_y > 0:
                self.mvt_x = -self.mvt_speed
            else:
                self.mvt_x = self.mvt_speed

    def is_over(self):
        if pygame.time.get_ticks() - self.birth >= self.duration:
            self.shooter.has_bullet = False
            return 1
        else:
            return 0

    def is_out_of_bounds(self, screen):
        if self.x < 0 or self.x > screen.get_width() or self.y < 0 or self.y > screen.get_height():
            self.shooter.has_bullet = False
            return 1
        else:
            return 0

    def is_in_wall(self, maze):
        for wall in maze.walls:
            if wall.contains(self.hit_box):
                return 1
        return 0
