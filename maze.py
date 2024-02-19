import pygame


class Maze:
    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

    def mirror_walls_vertically(self, width):
        temp_walls = list(self.walls)
        for wall in self.walls:
            mirrored_wall = pygame.Rect(width - wall[0] - wall[2], wall[1], wall[2], wall[3])
            temp_walls.append(mirrored_wall)
        self.walls = temp_walls

    def mirror_walls_horizontally(self, game_height_start, height):
        temp_walls = list(self.walls)
        for wall in self.walls:
            mirrored_wall = pygame.Rect(wall[0], height + game_height_start - wall[1] - wall[3], wall[2], wall[3])
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

    def draw_map(self, screen, background):
        if background == 0:
            screen.fill((0, 0, 0))
            screen.blit(self.scaled("assets/backgrounds/dungeon_background.png"), (0, 0))
            # screen.blit(self.scaled("assets/walls/left_wall.png"), (130, 190))
            # screen.blit(self.scaled("assets/walls/right_wall.png"), (1020, 190))

            # obstacles
            # screen.blit(self.scaled("assets/walls/horizontal_double_wall.png"), (382, 317))
            # screen.blit(self.scaled("assets/walls/horizontal_double_wall.png"), (765, 384))
            # screen.blit(self.scaled("assets/walls/vertical_double_wall.png"), (635, 125))
            # screen.blit(self.scaled("assets/walls/vertical_double_wall.png"), (570, 512))
