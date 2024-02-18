import pygame


class Menu:
    def __init__(self, screen):
        self.in_menu = True
        self.screen = screen

        # screen dimensions
        HEIGHT = screen.get_height()
        WIDTH = screen.get_width()

        # colors
        red = (144, 38, 10)
        yellow = (216, 169, 64)
        white = (255, 255, 255)
        green = (28, 92, 72)
        blue = (144, 204, 232)

        title_font = pygame.font.Font('assets/RPGgame.ttf', 120)
        self.title = title_font.render('Wizards', True, white, None)
        self.title_w = self.title.get_width()
        self.title_x = WIDTH // 2 - (self.title_w // 2)
        self.title_y = HEIGHT // 6

        subtitle_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 50)
        self.subtitle = subtitle_font.render('choose game mode:', True, white, None)
        self.subtitle_w = self.subtitle.get_width()
        self.subtitle_h = self.subtitle.get_height()
        self.subtitle_x = WIDTH // 2 - (self.subtitle.get_width() // 2)
        self.subtitle_y = 2 * HEIGHT // 6

        options_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 35)
        self.game_mode0 = options_font.render('Projectile Bounce', True, white, None)
        self.gm0_w = self.game_mode0.get_width()
        self.gm0_h = self.game_mode0.get_height()
        self.gm0_x = WIDTH // 2 - self.gm0_w // 2
        self.gm0_y = 3 * HEIGHT // 6

        self.game_mode1 = options_font.render('Projectile Telekinesis', True, white, None)
        self.gm1_w = self.game_mode1.get_width()
        self.gm1_h = self.game_mode1.get_height()
        self.gm1_x = WIDTH // 2 - self.gm1_w // 2
        self.gm1_y = 3.25 * HEIGHT // 6 + self.gm1_h

        quit_font = options_font
        self.quit = quit_font.render('Quit Game', True, white, None)
        self.quit_w = self.quit.get_width()
        self.quit_h = self.quit.get_height()
        self.quit_x = WIDTH // 2 - (self.quit_w // 2)
        self.quit_y = 5 * HEIGHT // 6

        credits_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 30)
        self.credits_screen = 0
        self.credits = credits_font.render('Credits', True, white, None)
        self.credits_w = self.credits.get_width()
        self.credits_h = self.credits.get_height()
        self.credits_x = WIDTH - 1.5 * self.credits_w
        self.credits_y = HEIGHT - 2 * self.credits_h

        back_font = credits_font
        self.back = back_font.render('Back', True, white, None)
        self.back_w = self.back.get_width()
        self.back_h = self.back.get_height()
        self.back_x = WIDTH // 2 - (self.back_w // 2)
        self.back_y = 11 * HEIGHT // 12

        names_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 60)
        self.rubens = names_font.render('Rubens Takashi Maruoka Vieira', True, white, None)
        self.rubens_w = self.rubens.get_width()
        self.rubens_h = self.rubens.get_height()
        self.rubens_x = WIDTH // 2 - (self.rubens_w // 2)
        self.rubens_y = 2 * HEIGHT // 12

        self.matheus = names_font.render('Matheus Takashi Maruoka Vieira', True, white, None)
        self.matheus_w = self.matheus.get_width()
        self.matheus_h = self.matheus.get_height()
        self.matheus_x = WIDTH // 2 - (self.matheus_w // 2)
        self.matheus_y = 5 * HEIGHT // 12

        self.vinicius = names_font.render('Vinicius Castro Coutinho', True, white, None)
        self.vinicius_w = self.vinicius.get_width()
        self.vinicius_h = self.vinicius.get_height()
        self.vinicius_x = WIDTH // 2 - (self.vinicius_w // 2)
        self.vinicius_y = 8 * HEIGHT // 12

    def status(self):
        return self.in_menu

    def turn_off(self):
        self.in_menu = False

    # check if the mouse is in "gm0" range
    def in_gm0(self):
        return (self.gm0_x <= pygame.mouse.get_pos()[0] <= self.gm0_x + self.gm0_w and
                self.gm0_y <= pygame.mouse.get_pos()[1] <= self.gm0_y + self.gm0_h)

    # check if the mouse is in "gm1" range
    def in_gm1(self):
        return (self.gm1_x <= pygame.mouse.get_pos()[0] <= self.gm1_x + self.gm1_w and
                self.gm1_y <= pygame.mouse.get_pos()[1] <= self.gm1_y + self.gm1_h)

    # check if the mouse is in "credits" range
    def in_credits(self):
        return (self.credits_x <= pygame.mouse.get_pos()[0] <= self.credits_x + self.credits_w and
                self.credits_y <= pygame.mouse.get_pos()[1] <= self.credits_y + self.credits_h)

    # check if the mouse is in "quit" range
    def in_quit(self):
        return (self.quit_x <= pygame.mouse.get_pos()[0] <= self.quit_x + self.quit_w and
                self.quit_y <= pygame.mouse.get_pos()[1] <= self.quit_y + self.quit_h)

    # check if the mouse is in "back" range
    def in_back(self):
        return (self.credits_screen and
                self.back_x <= pygame.mouse.get_pos()[0] <= self.back_x + self.back_w and
                self.back_y <= pygame.mouse.get_pos()[1] <= self.back_y + self.back_h)

    # check if the mouse is selecting
    def selecting(self, screen, color, rect_x, rect_y, rect_width, rect_height, thickness):
        pygame.draw.rect(screen, color, (rect_x - thickness, rect_y - thickness,
                                         rect_width + 2 * thickness, rect_height + 2 * thickness), thickness)

    # creates initial menu
    def menu_background(self, screen):
        screen.fill((0, 0, 0))
        scenario0 = pygame.image.load("assets/backgrounds/title_screen.png")
        scaled_image = pygame.transform.scale(scenario0, (scenario0.get_width() * 4, scenario0.get_height() * 4))
        screen.blit(scaled_image, (0, 0))

    def initial_menu(self, screen, thickness, color):
        screen.blit(self.title, (self.title_x, self.title_y))
        screen.blit(self.subtitle, (self.subtitle_x, self.subtitle_y))
        if self.in_gm0():
            self.selecting(screen, color, self.gm0_x, self.gm0_y, self.gm0_w, self.gm0_h, thickness)
            screen.blit(self.game_mode0, (self.gm0_x, self.gm0_y))
        else:
            screen.blit(self.game_mode0, (self.gm0_x, self.gm0_y))

        if self.in_gm1():
            self.selecting(screen, color, self.gm1_x, self.gm1_y, self.gm1_w, self.gm1_h, thickness)
            screen.blit(self.game_mode1, (self.gm1_x, self.gm1_y))
        else:
            screen.blit(self.game_mode1, (self.gm1_x, self.gm1_y))

        if self.in_quit():
            self.selecting(screen, color, self.quit_x, self.quit_y, self.quit_w, self.quit_h, thickness)
            screen.blit(self.quit, (self.quit_x, self.quit_y))
        else:
            screen.blit(self.quit, (self.quit_x, self.quit_y))
        if self.in_credits():
            self.selecting(screen, color, self.credits_x, self.credits_y, self.credits_w,
                           self.credits_h, thickness)
            screen.blit(self.credits, (self.credits_x, self.credits_y))
        else:
            screen.blit(self.credits, (self.credits_x, self.credits_y))

    # creates credits menu
    def credits_menu(self, screen, thickness, color):
        screen.blit(self.matheus, (self.matheus_x, self.matheus_y))
        screen.blit(self.rubens, (self.rubens_x, self.rubens_y))
        screen.blit(self.vinicius, (self.vinicius_x, self.vinicius_y))
        if self.in_back():
            self.selecting(screen, color, self.back_x, self.back_y, self.back_w,
                           self.back_h, thickness)
            screen.blit(self.back, (self.back_x, self.back_y))
        else:
            screen.blit(self.back, (self.back_x, self.back_y))
