import pygame

pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks[0].get_name())

screen = pygame.display.set_mode((500, 500))
start = 1

rect = pygame.Rect(0, 0, 30, 30)
print(rect.bottomleft)
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
        if event.type == pygame.JOYAXISMOTION:
            if abs(event.value) > 0.5:
                print(event)

    pygame.draw.rect(screen, (255, 0, 0), rect)
    screen.fill((0, 0, 0))
    pygame.display.flip()
