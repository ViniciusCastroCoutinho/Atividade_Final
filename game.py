import pygame
from maze import Maze
from tank import Tank
from bullet import Bullet


class Game:
    def __init__(self):
        self.game_start = True

    def game_running(self):
        if self.game_start:
            pygame.init()

            RED = (144, 38, 10)
            YELLOW = (216, 169, 64)

            WIDTH = 1280
            HEIGHT = 720
            HALF_W = WIDTH // 2
            GAME_HEIGHT_START = 70
            HALF_GH = (HEIGHT - GAME_HEIGHT_START) // 2

            size = (WIDTH, HEIGHT)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("COMBAT")

            # game mode
            game_mode = 'bullet bounce'

            # tanks
            tanks = []
            p1 = pygame.Rect(HALF_W, HALF_GH, 48, 48)

            # bullets
            bullets = []

            # walls
            middle_line = pygame.Rect(HALF_W, GAME_HEIGHT_START, 1, 720 - GAME_HEIGHT_START)
            w1 = pygame.Rect(0, GAME_HEIGHT_START, 24, 720 - GAME_HEIGHT_START)
            w2 = pygame.Rect(0, GAME_HEIGHT_START, WIDTH, 24)
            w3 = pygame.Rect(0, HEIGHT - 24, WIDTH, 24)
            w4 = pygame.Rect(800, HALF_GH, 96, 96)

            # maze
            maze = Maze()
            maze.add_wall(middle_line)
            maze.add_wall(w1)
            maze.add_wall(w2)
            maze.add_wall(w3)
            maze.add_wall(w4)
            maze.mirror_walls(WIDTH)

            # Clock
            clock = pygame.time.Clock()

            while self.game_start:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_start = False

                screen.fill(RED)

                # drawing
                screen.fill(RED)
                pygame.draw.rect(screen, YELLOW, p1)  # so pra testar
                maze.maze_draw(screen, YELLOW)

                # update screen
                pygame.display.flip()
                clock.tick(60)
        else:
            pygame.quit()
