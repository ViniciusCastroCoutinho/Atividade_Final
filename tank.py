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
        self.ball_speed = 4
        self.sprite_sheet_image = pygame.image.load(sprite).convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.step_counter = 0
        self.magic = None
        self.crosshair_x = 17
        self.crosshair_y = -40
        self.new_action = 0

        # declaring player animation
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 15, 17, 3.5, (254, 254, 254)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

        # declaring magic animation
        if sprite == "assets/sprites/black_mage(1).png" or "assets/sprites/black_mage.png":
            self.magic = pygame.image.load("assets/sprites/black_ball.png")
        elif sprite == "assets/sprites/blue_mage(1).png" or "assets/sprites/blue_mage.png":
            self.magic = pygame.image.load("assets/sprites/blue_ball.png")
        elif sprite == "assets/sprites/red_mage(1).png" or "assets/sprites/red_mage.png":
            self.magic = pygame.image.load("assets/sprites/fireball_spritesheet.png")
        elif sprite == "assets/sprites/white_mage.png" or "assets/sprites/white_mage(1).png":
            self.magic = pygame.image.load("assets/sprites/white_ball.png")

        self.sprite_sheet_magic = self.magic.convert_alpha()
        self.sprite_sheet_magic_animation = spritesheet.SpriteSheet(self.sprite_sheet_magic)
        self.magic_list = []
        self.magic_steps = []
        self.magic_action = 0
        self.magic_animation_cooldown = 100
        self.magic_frame = 0
        self.magic_step_counter = 0

        for animation in self.magic_steps:
            temp_magic_list = []
            for _ in range(animation):
                temp_magic_list.append(self.sprite_sheet_magic_animation.get_image
                                       (self.magic_step_counter, 15, 17, 3.5, (254, 254, 254)))
                self.magic_step_counter += 1
            self.magic_list.append(temp_magic_list)


        # control scheme
        if control_scheme == 0:
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.shoot = pygame.K_SPACE
        elif control_scheme == 1:
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.shoot = pygame.K_RSHIFT
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

    def crosshair(self, x, y):
        self.crosshair_x = x
        self.crosshair_y = y

    def stop_animation(self, action):
        if action == 8:
            self.new_action = 0
            self.frame = 0
        elif action == 9:
            self.new_action = 1
            self.frame = 0
        elif action == 10:
            self.new_action = 2
            self.frame = 0
        elif action == 11:
            self.new_action = 3
            self.frame = 0
        elif action == 12:
            self.new_action = 4
            self.frame = 0
        elif action == 13:
            self.new_action = 5
            self.frame = 0
        elif action == 14:
            self.new_action = 6
            self.frame = 0
        elif action == 15:
            self.new_action = 7
            self.frame = 0
        return self.new_action




