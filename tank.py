import pygame
import spritesheet


class Tank:
    def __init__(self, sizex, sizey, positionx, positiony, sprite, control_scheme):
        self.sizex = sizex
        self.sizey = sizey
        self.positionx = positionx
        self.positiony = positiony
        self.rect = pygame.Rect(self.sizex, self.sizey, self.positionx, self.positiony)
        self.mvt_speed = 4

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
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 15, 17, 4, (254, 254, 254)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

        # control scheme
        if control_scheme == 0:
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.shoot = pygame.K_RSHIFT
        elif control_scheme == 1:
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.shoot = pygame.K_SPACE
        elif control_scheme == 2:
            pass
        elif control_scheme == 3:
            pass
        else:
            print(f"invalid control scheme '{control_scheme}'")

    def move_up(self):
        self.positiony -= self.mvt_speed

    def move_down(self):
        self.positiony += self.mvt_speed

    def move_right(self):
        self.positionx += self.mvt_speed

    def move_left(self):
        self.positionx -= self.mvt_speed
