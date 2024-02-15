import pygame
import spritesheet


class Tank:
    def __init__(self, sizex, sizey, positionx, positiony, sprite):
        self.sizex = sizex
        self.sizey = sizey
        self.positionx = positionx
        self.positiony = positiony
        self.rect = pygame.Rect(self.sizex, self.sizey, self.positionx, self.positiony)
        self.sprite_sheet_image = pygame.image.load(sprite).convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.step_counter = 0

        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self. sprite_sheet.get_image(self.step_counter, 15, 17, 4, (0, 0, 0)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

    def move_right(self):
        self.positionx += 5

    def move_left(self):
        self.positionx -= 5

    def move_up(self):

        self.positiony -= 5

    def move_down(self):

        self.positiony += 5

