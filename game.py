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
            p1 = Tank(90, 90, 5, 5, "sprites/black_mage.png")

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
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            p1.action = 0
                        if event.key == pygame.K_UP and event.key == pygame.K_UP:
                            p1.action = 1
                        if event.key == pygame.K_RIGHT:
                            p1.action = 2
                        if event.key == pygame.K_RIGHT and event.key == pygame.K_DOWN:
                            p1.action = 3
                            p1.move_down()
                            p1.move_right()
                        if event.key == pygame.K_DOWN:
                            p1.action = 4
                        if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                            p1.action = 5
                        if event.key == pygame.K_LEFT:
                            p1.action = 6
                        if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                            p1.action = 7

                screen.fill(RED)

                # drawing
                screen.fill(RED)
                pygame.draw.rect(screen, YELLOW, p1)  # so pra testar
                maze.maze_draw(screen, YELLOW)

                # update animation
                current_time = pygame.time.get_ticks()
                if current_time - p1.last_update >= p1.animation_cooldown:
                    p1.frame += 1
                    p1.last_update = current_time
                    if p1.frame >= len(p1.animation_list[p1.action]):
                        p1.frame = 0

                # show frame
                screen.blit(p1.animation_list[p1.action][p1.frame], (0, 0))

                # update screen
                pygame.display.flip()
                clock.tick(60)
        else:
            pygame.quit()
