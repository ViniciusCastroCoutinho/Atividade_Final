import pygame


class Maze:
    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

    def mirror_walls_vertically(self, width):
        temp_walls = list(self.walls)
        for wall in self.walls:
            if wall[0] == 199:
                mirrored_wall = pygame.Rect(width - wall[0] - wall[2], wall[1], wall[2], wall[3])
                temp_walls.append(mirrored_wall)
            elif wall[0] == 128:
                mirrored_wall = pygame.Rect(width - wall[0] - wall[2], wall[1], wall[2], wall[3])
                temp_walls.append(mirrored_wall)
            elif wall[0] == 385:
                mirrored_wall = pygame.Rect(width - wall[0] - wall[2] - 3, wall[1] + 67, wall[2], wall[3])
                temp_walls.append(mirrored_wall)
            elif wall[0] == 390:
                mirrored_wall = pygame.Rect(width - wall[0] - wall[2], wall[1], wall[2], wall[3])
                temp_walls.append(mirrored_wall)
        self.walls = temp_walls

    def mirror_walls_horizontally(self, game_height_start, height):
        temp_walls = list(self.walls)
        for wall in self.walls:
            if wall[0] == 641:
                mirrored_wall = pygame.Rect(wall[0] - 65, height + game_height_start - wall[1] - wall[3] + 40, wall[2],
                                            wall[3])
                temp_walls.append(mirrored_wall)
            elif wall[0] == 128:
                mirrored_wall = pygame.Rect(wall[0], height + game_height_start - wall[1] - wall[3] + 80, wall[2],
                                            wall[3])
                temp_walls.append(mirrored_wall)
            elif wall[0] == 199:
                mirrored_wall = pygame.Rect(wall[0], height + game_height_start - wall[1] - wall[3], wall[2],
                                            wall[3] + 50)
                temp_walls.append(mirrored_wall)
            elif wall[0] == 709 or wall[0] == 512:
                mirrored_wall = pygame.Rect(wall[0], height + game_height_start - wall[1] - wall[3] + 55, wall[2],
                                            wall[3])
                temp_walls.append(mirrored_wall)
        self.walls = temp_walls

    def mirror_wall(self, wall_name, mirror_line, screen, game_height_start):
        for wall in self.walls:
            if wall == wall_name:
                if mirror_line == 'ver':
                    mirrored_wall = pygame.Rect(screen.get_witdh() - wall[0] - wall[2], wall[1], wall[2], wall[3])
                    self.walls.append(mirrored_wall)
                    return
                elif mirror_line == 'hor':
                    mirrored_wall = pygame.Rect(wall[0], screen.get_height() + game_height_start - wall[1] - wall[3],
                                                wall[2], wall[3])
                    self.walls.append(mirrored_wall)
                    return
                else:
                    print(f"invalid mirror_line value {mirror_line} in maze")

    def collision(self, colliding_rect):
        return colliding_rect.collidelist(self.walls)

    def draw(self, screen, color):
        for wall in self.walls:
            pygame.draw.rect(screen, color, wall)

    def scaled(self, image):
        image = pygame.image.load(image)
        return pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))

    def draw_map(self, screen, map_type):
        if map_type == 0:
            screen.fill((0, 0, 0))
            screen.blit(self.scaled("assets/backgrounds/dungeon_background.png"), (0, 0))
        elif map_type == 1:
            screen.fill((0, 0, 0))
            screen.blit(self.scaled("assets/backgrounds/dungeon_background.png"), (0, 0))
            screen.blit(self.scaled("assets/walls/double_horizontal_lower.png"), (385, 380))
            screen.blit(self.scaled("assets/walls/double_horizontal_lower.png"), (765, 448))
            screen.blit(self.scaled("assets/walls/vertical_double_wall.png"), (635, 125))
            screen.blit(self.scaled("assets/walls/vertical_double_wall.png"), (570, 512))
            screen.blit(self.scaled("assets/walls/left_wall.png"), (130, 253))
            screen.blit(self.scaled("assets/walls/right_wall.png"), (1025, 253))
        elif map_type == 2:
            screen.fill((0, 0, 0))
            screen.blit(self.scaled("assets/backgrounds/dungeon_background.png"), (0, 0))
            screen.blit(self.scaled("assets/walls/left_wall.png"), (130, 253))
            screen.blit(self.scaled("assets/walls/right_wall.png"), (1025, 253))
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (705, 253))  # 1
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (506, 253))  # 1
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (384, 380))  # 2
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (828, 380))  # 2
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (705, 573))  # 3
            screen.blit(self.scaled("assets/walls/wall_lower.png"), (506, 573))  # 3

    def draw_obstacle(self, screen, map_type):
        if map_type == 0:
            pass
        elif map_type == 1:
            screen.blit(self.scaled("assets/walls//right_wall_upper.png"), (1025, 190))
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (1089, 509))
            screen.blit(self.scaled("assets/walls/left_wall_upper.png"), (130, 190))
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (126, 509))
            screen.blit(self.scaled("assets/walls/double_horizontal_upper.png"), (385, 317))
            screen.blit(self.scaled("assets/walls/double_horizontal_upper.png"), (765, 384))
        elif map_type == 2:
            screen.blit(self.scaled("assets/walls//right_wall_upper.png"), (1025, 190))
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (1089, 509))
            screen.blit(self.scaled("assets/walls/left_wall_upper.png"), (130, 190))
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (126, 509))
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (705, 189))  # 1
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (506, 189))  # 1
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (384, 316))  # 2
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (828, 316))  # 2
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (705, 509))  # 3
            screen.blit(self.scaled("assets/walls/wall_upper.png"), (506, 509))  # 3
