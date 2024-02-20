import pygame
import spritesheet
import random


class Tank:
    def __init__(self, width, height, positionx, positiony, skin, magic, control_scheme, controller=None):
        self.width = width
        self.height = height
        self.positionx = positionx
        self.positiony = positiony
        self.hit_box = pygame.Rect(self.positionx, self.positiony, self.width, self.height)
        self.mvt_speed = 4
        self.control_scheme = control_scheme
        self.score = 0
        self.respawn_cooldown = 2000
        self.time_of_death = 0
        self.dead = False
        if controller is not None:
            self.controller = controller

        self.skin = skin
        if skin == 0:
            sprite = "assets/sprites/black_mage.png"
        elif skin == 1:
            sprite = "assets/sprites/blue_mage.png"
        elif skin == 2:
            sprite = "assets/sprites/red_mage.png"
        elif skin == 3:
            sprite = "assets/sprites/white_mage.png"
        elif skin == 4:
            sprite = "assets/sprites/green_mage.png"
        else:
            sprite = "assets/sprites/green_mage.png"

        if magic == 0:
            self.magic = "assets/sprites/black_ball.png"
        elif magic == 1:
            self.magic = "assets/sprites/blue_ball.png"
        elif magic == 2:
            self.magic = "assets/sprites/fireball_spritesheet.png"
        elif magic == 3:
            self.magic = "assets/sprites/white_ball.png"
        elif magic == 4:
            self.magic = "assets/sprites/earth_ball.png"

        self.sprite_sheet_image = pygame.image.load(sprite).convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.step_counter = 0

        # shooting
        self.has_bullet = False
        self.crosshair = pygame.Rect(0, 0, 20, 20)
        self.crosshair.centerx = self.hit_box.centerx
        self.crosshair.centery = self.hit_box.centery - 1.5 * self.height
        self.new_action = 0

        # declaring player animation
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 15, 17, 3.5, (254, 254, 254)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

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
            self.shoot = 0
            self.axis_x = self.controller.get_axis(0)
            self.axis_y = self.controller.get_axis(1)
        else:
            print(f"invalid control scheme '{control_scheme}'")

    def move_up(self):
        self.positiony -= self.mvt_speed
        self.hit_box[1] -= self.mvt_speed

    def move_down(self):
        self.positiony += self.mvt_speed
        self.hit_box[1] += self.mvt_speed

    def move_right(self, ):
        self.positionx += self.mvt_speed
        self.hit_box[0] += self.mvt_speed

    def move_left(self):
        self.positionx -= self.mvt_speed
        self.hit_box[0] -= self.mvt_speed

    def get_axis_y(self):
        self.axis_y = self.controller.get_axis(1)
        return self.axis_y

    def get_axis_x(self):
        self.axis_x = self.controller.get_axis(0)
        return self.axis_x

    def crosshair_update(self, direction1):
        if direction1 == 'up':
            self.crosshair.centerx = self.hit_box.centerx
            self.crosshair.centery = self.hit_box.centery - 1.5 * self.height
        elif direction1 == 'down':
            self.crosshair.centerx = self.hit_box.centerx
            self.crosshair.centery = self.hit_box.centery + 1.5 * self.height
        elif direction1 == 'right':
            self.crosshair.centerx = self.hit_box.centerx + 1.5 * self.width
            self.crosshair.centery = self.hit_box.centery
        elif direction1 == '+right':
            self.crosshair.centerx += 1.5 * self.width
        elif direction1 == 'left':
            self.crosshair.centerx = self.hit_box.centerx - 1.5 * self.width
            self.crosshair.centery = self.hit_box.centery
        elif direction1 == '+left':
            self.crosshair.centerx -= 1.5 * self.width

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

    def bullet_collision(self, colliding_rect):
        if colliding_rect.hit_box.colliderect(self.hit_box):
            return 1
        else:
            return 0

    def death(self):
        self.dead = True
        self.time_of_death = pygame.time.get_ticks()

    def respawn(self, screen, maze):
        x = random.randint(0, screen.get_width())
        y = random.randint(100, screen.get_height())
        temp_rect = pygame.Rect(x, y, self.width, self.height)
        if maze.collision(temp_rect) != -1:
            invalid = 1
            while invalid:
                x = random.randint(0, screen.get_width())
                y = random.randint(100, screen.get_height())
                temp_rect = pygame.Rect(x, y, self.width, self.height)
                if maze.collision(temp_rect) == -1:
                    invalid = 0
        self.positionx = x
        self.positiony = y
        self.action = 0
        self.hit_box = temp_rect
