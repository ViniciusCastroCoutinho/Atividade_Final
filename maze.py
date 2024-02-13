import pygame


class Maze:
    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

    def mirror_walls(self, width):
        temp_walls = list(self.walls)
        for wall in self.walls:
            mirrored_wall = pygame.Rect(width - wall[0] - wall[2], wall[1], wall[2], wall[3])
            temp_walls.append(mirrored_wall)
        self.walls = temp_walls

    def maze_collision(self, colliding_rect):
        return colliding_rect.collidelist(self.walls)

    def maze_draw(self, screen, color):
        for wall in self.walls:
            pygame.draw.rect(screen, color, wall)
