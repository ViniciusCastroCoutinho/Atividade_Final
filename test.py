import  pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
start = 1

rect = pygame.Rect(0, 0, 30, 30)
print(rect.bottomleft)
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    pygame.draw.rect(screen, (255, 0, 0), rect)
    screen.fill((0, 0, 0))
    pygame.display.flip()