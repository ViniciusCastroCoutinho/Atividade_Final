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
        self.animation_dash_list = []
        self.animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
        self.dash_action = 0
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.animation_dash_cooldown = 30
        self.frame = 0
        self.dash_frame = 0
        self.step_counter = 0
        self.step_counter_dash = 0
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 15, 17, 3.5, (254, 254, 254)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)
        # tentativa de animação do dash
        for dash_animation in self.animation_steps:
            temp_dash_img_list = []
            for _ in range(dash_animation):
                temp_dash_img_list.append(
                    self.sprite_sheet.get_image(self.step_counter_dash, 15, 17, 3.5, (254, 254, 254, 127)))
                self.step_counter_dash += 1
            self.animation_dash_list.append(temp_dash_img_list)

        # control scheme
        if control_scheme == 0:
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.shoot = pygame.K_SPACE
            self.dash = pygame.K_LSHIFT
        elif control_scheme == 1:
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.shoot = pygame.K_RSHIFT
            self.dash = pygame.K_RCTRL
        elif control_scheme == 2:
            pass
        elif control_scheme == 3:
            pass
        else:
            print(f"invalid control scheme '{control_scheme}'")

    def move_up(self):
        self.positiony -= self.mvt_speed
        if self.positiony <= 146:
            self.positiony = 148

    def move_down(self):
        self.positiony += self.mvt_speed
        if self.positiony > 650:
            self.positiony = 648

    def move_right(self):
        self.positionx += self.mvt_speed
        if self.positionx >= 1227:
            self.positionx = 1226

    def move_left(self):
        self.positionx -= self.mvt_speed
        if self.positionx < 0:
            self.positionx = 1

