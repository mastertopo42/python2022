import pygame
from pygame.draw import circle

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100) # морда
circle(screen, (0, 154, 205), (160, 145), 10) # глаз
circle(screen, (0, 154, 205), (240, 145), 10) # глаз
circle(screen, (0, 0, 0), (162, 145), 5) # зрачок
circle(screen, (0, 0, 0), (238, 145), 5) # зрачок
circle(screen, (255, 255, 255), (200, 200), 40) # рот
circle(screen, (255, 255, 0), (200, 175), 40) # рот
pygame.draw.rect(screen, (0, 0, 0), (220, 120, 50 - 10, 15 - 10), 0) # бровь
pygame.draw.rect(screen, (0, 0, 0), (140, 120, 50 - 10, 15 - 10), 0) # бровь

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()