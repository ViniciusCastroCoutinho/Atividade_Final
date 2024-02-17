import pygame
from menu import Menu
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
            GAME_HEIGHT = HEIGHT - GAME_HEIGHT_START
            HALF_GH_LENGHT = GAME_HEIGHT // 2
            HALF_GH_POS = GAME_HEIGHT_START + (GAME_HEIGHT // 2)


            size = (WIDTH, HEIGHT)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("COMBAT")

            # game mode
            game_mode = 0

            # menu screen
            menu = Menu(screen)

            # walls
            std_dimension = 24
            w90 = pygame.Rect(0, GAME_HEIGHT_START, std_dimension, GAME_HEIGHT)
            w91 = pygame.Rect(WIDTH - std_dimension, GAME_HEIGHT_START, std_dimension, GAME_HEIGHT)
            w92 = pygame.Rect(0, GAME_HEIGHT_START, WIDTH, std_dimension)
            w93 = pygame.Rect(0, HEIGHT - std_dimension, WIDTH, std_dimension)
            w1 = pygame.Rect(HALF_W - std_dimension, HALF_GH_LENGHT // 2, std_dimension, 4 * std_dimension)
            w2 = pygame.Rect(HALF_W // 2, HALF_GH_POS - std_dimension, 4 * std_dimension, std_dimension)
            w3 = pygame.Rect(HALF_W // 4, 2 * HALF_GH_POS // 3, 2 * std_dimension, std_dimension)
            w4 = pygame.Rect(w3[0] + w3[2] // 2, w3[1], w3[2] // 2, HALF_GH_POS - w3[1])

            # maze
            maze = Maze()
            maze.add_wall(w1)
            maze.add_wall(w2)
            maze.add_wall(w3)
            maze.add_wall(w4)
            maze.mirror_walls_horizontally(GAME_HEIGHT_START, HEIGHT)
            maze.mirror_walls_vertically(WIDTH)
            maze.add_wall(w90)
            maze.add_wall(w91)
            maze.add_wall(w92)
            maze.add_wall(w93)

            # players
            players = []
            p_size = 90
            p1 = Tank(p_size, p_size, std_dimension, HALF_GH_POS, "sprites/black_mage(1).png", 0)
            p2 = Tank(p_size, p_size, WIDTH - std_dimension - p_size, HALF_GH_POS, "sprites/red_mage(1).png", 9)
            players.append(p1)
            players.append(p2)

            # joysticks
            # joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

            # bullets
            bullets = []

            # Clock
            clock = pygame.time.Clock()

            while self.game_start:
                # player movement
                keys = pygame.key.get_pressed()
                for player in players:
                    if keys[player.up]:
                        player.action = 0
                        player.move_up()
                        if keys[player.right]:
                            player.action = 1
                            player.move_right()
                        elif keys[player.left]:
                            player.action = 7
                            player.move_left()
                    elif keys[player.down]:
                        player.action = 4
                        player.move_down()
                        if keys[player.right]:
                            player.action = 3
                            player.move_right()
                        elif keys[player.left]:
                            player.action = 5
                            player.move_left()
                    elif keys[player.right]:
                        player.action = 2
                        player.move_right()
                    elif keys[player.left]:
                        player.action = 6
                        player.move_left()

                # quit
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_start = False

                    # menu screen
                    if menu.status() is True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == pygame.mouse.get_pressed(3)[0]:
                                if (menu.gm0_x <= pygame.mouse.get_pos()[0] <= menu.gm0_x + menu.gm0_w and
                                        menu.gm0_y <= pygame.mouse.get_pos()[1] <= menu.gm0_y + menu.gm0_h):
                                    game_mode = 0
                                    menu.turn_off()

                                elif (menu.gm1_x <= pygame.mouse.get_pos()[0] <= menu.gm1_x + menu.gm1_w and
                                        menu.gm1_y <= pygame.mouse.get_pos()[1] <= menu.gm1_y + menu.gm1_h):
                                    game_mode = 1
                                    menu.turn_off()

                                elif (menu.credits_x <= pygame.mouse.get_pos()[0] <= menu.credits_x + menu.credits_w and
                                        menu.credits_y <= pygame.mouse.get_pos()[1] <= menu.credits_y + menu.credits_h):
                                    menu.credits_screen = True

                                elif (menu.quit_x <= pygame.mouse.get_pos()[0] <= menu.quit_x + menu.quit_w and
                                        menu.quit_y <= pygame.mouse.get_pos()[1] <= menu.quit_y + menu.quit_h):
                                    self.game_start = False

                                elif (menu.credits_screen and
                                      menu.back_x <= pygame.mouse.get_pos()[0] <= menu.back_x + menu.back_w and
                                      menu.back_y <= pygame.mouse.get_pos()[1] <= menu.back_y + menu.back_h):
                                    menu.credits_screen = False

                # drawing
                if menu.status() is True:
                    screen.fill(RED)
                    if not menu.credits_screen:
                        screen.blit(menu.title, (menu.title_x, menu.title_y))
                        screen.blit(menu.subtitle, (menu.subtitle_x, menu.subtitle_y))
                        screen.blit(menu.game_mode0, (menu.gm0_x, menu.gm0_y))
                        screen.blit(menu.game_mode1, (menu.gm1_x, menu.gm1_y))
                        screen.blit(menu.quit, (menu.quit_x, menu.quit_y))
                        screen.blit(menu.credits, (menu.credits_x, menu.credits_y))
                    else:
                        screen.blit(menu.matheus, (menu.matheus_x, menu.matheus_y))
                        screen.blit(menu.rubens, (menu.rubens_x, menu.rubens_y))
                        screen.blit(menu.vinicius, (menu.vinicius_x, menu.vinicius_y))
                        screen.blit(menu.back, (menu.back_x, menu.back_y))

                else:
                    screen.fill(RED)
                    maze.maze_draw(screen, YELLOW)

                    # update animation
                    current_time = pygame.time.get_ticks()
                    for player in players:
                        if current_time - player.last_update >= player.animation_cooldown:
                            player.frame += 1
                            player.last_update = current_time
                            if player.frame >= len(player.animation_list[player.action]):
                                player.frame = 0

                        # show frame
                        screen.blit(player.animation_list[player.action][player.frame],
                                    (player.positionx, player.positiony))

                # update screen
                pygame.display.flip()
                clock.tick(60)
        else:
            pygame.quit()
