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
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            WIDTH = 1280
            HEIGHT = 720
            HALF_W = WIDTH // 2
            GAME_HEIGHT_START = 70
            GAME_HEIGHT = HEIGHT - GAME_HEIGHT_START
            HALF_GH_LENGTH = GAME_HEIGHT // 2
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
            map = 0
            w90 = pygame.Rect(0, GAME_HEIGHT_START, std_dimension, GAME_HEIGHT)
            w91 = pygame.Rect(WIDTH - std_dimension, GAME_HEIGHT_START, std_dimension, GAME_HEIGHT)
            w92 = pygame.Rect(0, GAME_HEIGHT_START + 70, WIDTH, std_dimension)  # Top wall
            w93 = pygame.Rect(0, HEIGHT - std_dimension, WIDTH, std_dimension)
            if map == 0:
                pass
            elif map == 1:
                w1 = pygame.Rect(HALF_W - std_dimension + 25, HALF_GH_LENGTH // 2 - 28,
                                 std_dimension + 40, 4 * std_dimension + 80)
                w2 = pygame.Rect(HALF_W // 2 + 65, HALF_GH_POS - std_dimension + 10, 4 *
                                 std_dimension + 27, std_dimension + 20)
                w3 = pygame.Rect(HALF_W // 4 - 32, 2 * HALF_GH_POS // 3 - 10, 2 *
                                 std_dimension + 77, std_dimension + 20)
                w4 = pygame.Rect(w3[0] + w3[2] // 2 + 9, w3[1], w3[2] // 2 - 8, HALF_GH_POS - w3[1])

            elif map == 2:
                w1 = pygame.Rect(HALF_W // 2 + 70, HALF_GH_POS - std_dimension + 10, 4 *
                                 std_dimension - 40, std_dimension - 5)
                w2 = pygame.Rect(WIDTH // 2 + 69, HALF_GH_POS - std_dimension - 118, 4 *
                                 std_dimension - 40, std_dimension - 5)
                w3 = pygame.Rect(HALF_W // 4 - 32, 2 * HALF_GH_POS // 3 - 10, 2 *
                                 std_dimension + 77, std_dimension + 20)
                w4 = pygame.Rect(w3[0] + w3[2] // 2 + 9, w3[1], w3[2] // 2 - 8, HALF_GH_POS - w3[1])
                w5 = pygame.Rect(w2[0] - 197, w2[1], w2[2], w2[3])

            # maze
            maze = Maze()
            if map == 0:
                maze.add_wall(w90)
                maze.add_wall(w91)
                maze.add_wall(w92)
                maze.add_wall(w93)
            elif map == 1:
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
            elif map == 2:
                maze.add_wall(w1)
                maze.add_wall(w2)
                maze.add_wall(w3)
                maze.add_wall(w4)
                maze.add_wall(w5)
                maze.mirror_walls_horizontally(GAME_HEIGHT_START, HEIGHT)
                maze.mirror_walls_vertically(WIDTH)
                maze.add_wall(w90)
                maze.add_wall(w91)
                maze.add_wall(w92)
                maze.add_wall(w93)

            # music & sounds
            pygame.mixer.music.load(
                'assets/sounds/[FREE] Kingdom Hearts - Dearly Beloved 8-Bit (No copyright music) #kingdomhearts'
                ' #8bit #remix #chill.mp3')
            pygame.mixer.music.play(90, 0.0, 1000)
            walk = pygame.mixer.Sound('assets/sounds/walk_sfx.wav')
            magic_summon = pygame.mixer.Sound('assets/sounds/bullet_summon.wav')
            magic_bounce = pygame.mixer.Sound('assets/sounds/bullet_bounce.wav')
            player_take_damage = pygame.mixer.Sound('assets/sounds/mage_damage.wav')

            # joysticks
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

            # players
            players = []
            p_size_x = 52.2
            p_size_y = 59.5

            p1 = Tank(p_size_x, p_size_y, std_dimension, HALF_GH_POS, 3, 3, 0)
            players.append(p1)

            p2 = Tank(p_size_x, p_size_y, WIDTH - std_dimension - p_size_x,
                      HALF_GH_POS, 2, 1, 1)
            players.append(p2)

            if len(joysticks) > 0:
                p3 = Tank(p_size_x, p_size_y, HALF_W,
                          HEIGHT - 1.5 * p_size_y, 0, 2, 2, joysticks[0])
                players.append(p3)
                if len(joysticks) > 1:
                    p4 = Tank(p_size_x, p_size_y, HALF_W,
                              HEIGHT - 1.5 * p_size_y, 1, 0, 2, joysticks[0])
                    players.append(p4)

            # bullets
            bullets = []

            # Clock
            clock = pygame.time.Clock()

            while self.game_start:
                current_time = pygame.time.get_ticks()
                keys = pygame.key.get_pressed()
                # player controls
                for player in players:
                    if player.control_scheme <= 1:
                        # movement
                        if keys[player.up]:
                            player.action = 8
                            player.move_up()
                            player.crosshair_update('up')
                            walk.play()
                            # telekinesis
                            if player.has_bullet and game_mode == 1:
                                for bullet in bullets:
                                    if bullet.shooter == player and bullet.mvt_x != 0:
                                        bullet.mvt_y -= bullet.mvt_speed / 25
                                        break
                            # check collision
                            if maze.collision(player.hit_box) != -1:
                                player.move_down()
                            # check for diagonal movement
                            if keys[player.right]:
                                player.action = 9
                                player.move_right()
                                player.crosshair_update('+right')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_left()

                            elif keys[player.left]:
                                player.action = 15
                                player.move_left()
                                player.crosshair_update('+left')
                            if maze.collision(player.hit_box) != -1:
                                player.move_right()

                        elif keys[player.down]:
                            player.action = 12
                            walk.play()
                            player.move_down()
                            player.crosshair_update('down')

                            if player.has_bullet and game_mode == 1:
                                for bullet in bullets:
                                    if bullet.shooter == player and bullet.mvt_x != 0:
                                        bullet.mvt_y += bullet.mvt_speed / 25
                                        break

                            if maze.collision(player.hit_box) != -1:
                                player.move_up()

                            if keys[player.right]:
                                player.action = 11
                                player.move_right()
                                player.crosshair_update('+right')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_left()

                            elif keys[player.left]:
                                player.action = 13
                                player.move_left()
                                player.crosshair_update('+left')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_right()

                        elif keys[player.right]:
                            player.action = 10
                            walk.play()
                            player.move_right()
                            player.crosshair_update('right')

                            if player.has_bullet and game_mode == 1:
                                for bullet in bullets:
                                    if bullet.shooter == player and bullet.mvt_y != 0:
                                        bullet.mvt_x += bullet.mvt_speed / 25
                                        break

                            if maze.collision(player.hit_box) != -1:
                                player.move_left()

                        elif keys[player.left]:
                            player.action = 14
                            walk.play()
                            player.move_left()
                            player.crosshair_update('left')

                            if player.has_bullet and game_mode == 1:
                                for bullet in bullets:
                                    if bullet.shooter == player and bullet.mvt_y != 0:
                                        bullet.mvt_x -= bullet.mvt_speed / 25
                                        break

                            if maze.collision(player.hit_box) != -1:
                                player.move_right()
                        else:
                            stop = player.stop_animation(player.action)
                            player.action = stop

                        # shooting
                        if keys[player.shoot]:
                            if player.has_bullet is False:
                                bullets.append(Bullet(player, 40, 40,
                                                      player.magic))
                                player.bullet_cooldown = current_time
                                magic_summon.play()
                                player.has_bullet = True
                    elif player.control_scheme == 2:
                        # movement
                        if abs(player.get_axis_y()) > 0.4:
                            if player.axis_y < 0:
                                player.action = 8
                                player.move_up()
                                player.crosshair_update('up')
                                walk.play()
                                if maze.collision(player.hit_box) != -1:
                                    player.move_down()
                                if abs(player.get_axis_x()) > 0.4:
                                    if player.axis_x > 0:
                                        player.action = 9
                                        player.move_right()
                                        player.crosshair_update('+right')
                                        if maze.collision(player.hit_box) != -1:
                                            player.move_left()
                                    elif player.axis_x < 0:
                                        player.action = 15
                                        player.move_left()
                                        player.crosshair_update('+left')
                                    if maze.collision(player.hit_box) != -1:
                                        player.move_right()
                            elif player.axis_y > 0:
                                player.action = 12
                                walk.play()
                                player.move_down()
                                player.crosshair_update('down')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_up()
                                if abs(player.get_axis_x()) > 0.4:
                                    if player.axis_x > 0:
                                        player.action = 11
                                        player.move_right()
                                        player.crosshair_update('+right')
                                        if maze.collision(player.hit_box) != -1:
                                            player.move_left()
                                    elif player.axis_x < 0:
                                        player.action = 13
                                        player.move_left()
                                        player.crosshair_update('+left')
                                        if maze.collision(player.hit_box) != -1:
                                            player.move_right()
                        elif abs(player.get_axis_x()) > 0.4:
                            if player.axis_x > 0:
                                player.action = 10
                                walk.play()
                                player.move_right()
                                player.crosshair_update('right')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_left()
                            elif player.axis_x < 0:
                                player.action = 14
                                walk.play()
                                player.move_left()
                                player.crosshair_update('left')
                                if maze.collision(player.hit_box) != -1:
                                    player.move_right()
                        else:
                            stop = player.stop_animation(player.action)
                            player.action = stop
                        # shooting
                        if player.controller.get_button(player.shoot):
                            if player.has_bullet is False:
                                print('shot fired')
                                bullets.append(Bullet(player, 40, 40, player.magic))
                                player.bullet_cooldown = current_time
                                magic_summon.play()
                                player.has_bullet = True

                # quit
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_start = False

                    # menu screen
                    if menu.status() is True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == pygame.mouse.get_pressed(3)[0]:
                                if menu.in_gm0():
                                    game_mode = 0
                                    menu.turn_off()
                                    pygame.mixer.music.pause()
                                    pygame.mixer.music.load('assets/sounds/RPG_MUSIC.mp3')
                                    pygame.mixer.music.play(-1, 1, 0)

                                elif menu.in_gm1():
                                    game_mode = 1
                                    menu.turn_off()
                                    pygame.mixer.music.pause()
                                    pygame.mixer.music.load('assets/sounds/RPG_MUSIC.mp3')
                                    pygame.mixer.music.play(-1, 1, 0)

                                elif menu.in_credits():
                                    menu.credits_screen = True

                                elif menu.in_quit():
                                    self.game_start = False

                                elif menu.in_back():
                                    menu.credits_screen = False

                # updating bullets
                temp_bullets = list(bullets)
                for bullet in bullets:
                    if bullet.is_over() or bullet.is_out_of_bounds(screen):
                        temp_bullets.remove(bullet)
                        bullet.shooter.has_bullet = False
                    else:
                        bullet.move_x()
                        if maze.collision(bullet.hit_box) != -1:
                            if game_mode == 0:
                                wall = maze.walls[maze.collision(bullet.hit_box)]
                                bullet.update_mvt_x(wall)
                                magic_bounce.play()
                            elif game_mode == 1:
                                temp_bullets.remove(bullet)
                                bullet.shooter.has_bullet = False
                                magic_bounce.play()

                        bullet.move_y()
                        if maze.collision(bullet.hit_box) != -1:
                            if game_mode == 0:
                                wall = maze.walls[maze.collision(bullet.hit_box)]
                                bullet.update_mvt_y(wall)
                            elif game_mode == 1:
                                if bullet in temp_bullets:
                                    temp_bullets.remove(bullet)
                                    bullet.shooter.has_bullet = False

                        # checking collision with enemies
                        for player in players:
                            if player != bullet.shooter and player.bullet_collision(bullet) and not player.dead:
                                temp_bullets.remove(bullet)
                                player_take_damage.play()
                                player.death()
                                bullet.shooter.score += 1
                                bullet.shooter.has_bullet = False
                bullets = temp_bullets

                # respawning dead players
                for player in players:
                    if player.dead:
                        if current_time - player.time_of_death >= player.respawn_cooldown:
                            player.respawn(screen, maze)
                            player.dead = False
                            player.crosshair_update('up')

                # drawing
                if menu.status() is True:
                    if not menu.credits_screen:
                        menu.menu_background(screen)
                        menu.initial_menu(screen, 3, WHITE)
                    else:
                        menu.menu_background(screen)
                        menu.credits_menu(screen, 3, WHITE)
                else:
                    # maze part 1
                    maze.draw_map(screen, map)
                    # maze.draw(screen, YELLOW)

                    # update animation walking
                    for player in players:
                        if current_time - player.last_update >= player.animation_cooldown:
                            player.frame += 1
                            player.last_update = current_time
                            if player.frame >= len(player.animation_list[player.action]):
                                player.frame = 0

                        # show frame
                        if not player.dead:
                            # pygame.draw.rect(screen, BLACK, player.hit_box)  # hit_box
                            screen.blit(player.animation_list[player.action][player.frame],
                                        (player.positionx, player.positiony))
                            pygame.draw.rect(screen, RED, player.crosshair)

                    # update bullet
                    for bullet in bullets:
                        if current_time - bullet.last_update >= bullet.animation_cooldown:
                            bullet.frame += 1
                            bullet.last_update = current_time
                            if bullet.frame >= len(bullet.animation_list[bullet.action]):
                                bullet.frame = 0
                        # show frame
                        # pygame.draw.rect(screen, (0, 0, 0), bullet.hit_box)  # hit_box
                        screen.blit(bullet.animation_list[bullet.action][bullet.frame],
                                    (bullet.x, bullet.y))

                    # draw maze part2
                    maze.draw_obstacle(screen, map)

                    # draw score
                    menu.draw_score(screen, players)
                # update screen
                pygame.display.flip()
                clock.tick(60)
        else:
            pygame.quit()
