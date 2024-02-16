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
        green = (28, 92, 72)
        blue = (144, 204, 232)

        title_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 120)
        self.title = title_font.render('COMBAT', True, yellow, red)
        self.title_w = self.title.get_width()
        self.title_x = WIDTH // 2 - (self.title_w // 2)
        self.title_y = HEIGHT // 6

        subtitle_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 50)
        self.subtitle = subtitle_font.render('choose game mode:', True, yellow, red)
        self.subtitle_w = self.subtitle.get_width()
        self.subtitle_h = self.subtitle.get_height()
        self.subtitle_x = WIDTH // 2 - (self.subtitle.get_width() // 2)
        self.subtitle_y = 2 * HEIGHT // 6

        options_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 35)
        self.game_mode0 = options_font.render('Projectile Bounce', True, red, yellow)
        self.gm0_w = self.game_mode0.get_width()
        self.gm0_h = self.game_mode0.get_height()
        self.gm0_x = WIDTH // 2 - self.gm0_w // 2
        self.gm0_y = 3 * HEIGHT // 6

        self.game_mode1 = options_font.render('Projectile Telekinesis', True, red, yellow)
        self.gm1_w = self.game_mode1.get_width()
        self.gm1_h = self.game_mode1.get_height()
        self.gm1_x = WIDTH // 2 - self.gm1_w // 2
        self.gm1_y = 3.25 * HEIGHT // 6 + self.gm1_h

        quit_font = options_font
        self.quit = quit_font.render('Quit Game', True, red, yellow)
        self.quit_w = self.quit.get_width()
        self.quit_h = self.quit.get_height()
        self.quit_x = WIDTH // 2 - (self.quit_w // 2)
        self.quit_y = 5 * HEIGHT // 6

        credits_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 30)
        self.credits_screen = 0
        self.credits = credits_font.render('Credits', True, red, yellow)
        self.credits_w = self.credits.get_width()
        self.credits_h = self.credits.get_height()
        self.credits_x = WIDTH - 1.5 * self.credits_w
        self.credits_y = HEIGHT - 2 * self.credits_h

        back_font = credits_font
        self.back = back_font.render('Back', True, red, yellow)
        self.back_w = self.back.get_width()
        self.back_h = self.back.get_height()
        self.back_x = WIDTH // 2 - (self.back_w // 2)
        self.back_y = 11 * HEIGHT // 12

        names_font = pygame.font.Font('assets/VCR_OSD_MONO_1.001.ttf', 60)
        self.rubens = names_font.render('Rubens Takashi Maruoka Vieira', True, yellow, red)
        self.rubens_w = self.rubens.get_width()
        self.rubens_h = self.rubens.get_height()
        self.rubens_x = WIDTH // 2 - (self.rubens_w // 2)
        self.rubens_y = 2 * HEIGHT // 12

        self.matheus = names_font.render('Matheus Takashi Maruoka Vieira', True, yellow, red)
        self.matheus_w = self.matheus.get_width()
        self.matheus_h = self.matheus.get_height()
        self.matheus_x = WIDTH // 2 - (self.matheus_w // 2)
        self.matheus_y = 5 * HEIGHT // 12

        self.vinicius = names_font.render('Vinicius Castro Coutinho', True, yellow, red)
        self.vinicius_w = self.vinicius.get_width()
        self.vinicius_h = self.vinicius.get_height()
        self.vinicius_x = WIDTH // 2 - (self.vinicius_w // 2)
        self.vinicius_y = 8 * HEIGHT // 12

    def status(self):
        return self.in_menu

    def turn_off(self):
        self.in_menu = False

