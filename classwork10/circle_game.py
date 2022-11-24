from math import sin, cos
from random import randint
import pygame
from pygame.draw import *


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

speed_min = 5
speed_max = 10


def collision(obj_db, mouse_butt, mouse_position):
    """
    проверяет попадания по объектам из obj_db ()
    
    :param obj_db: база данных с объектами
    :param mouse_butt: кномка мыши которая бфл анажата
    :param mouse_position: масссив с координатами мыши
    :return: обновлённая базат данных
    """
    mouse_butt += 1
    for itera in range(len(obj_db) - 1, -1, -1):
        lenght = (obj_db[itera].pos[0] - mouse_position[0]) ** 2 + (obj_db[itera].pos[1] - mouse_position[1])  # расстояние
        if lenght <= obj_db[itera].rad ** 2:
            global score
            score += obj_db[itera].score
            del obj_db[itera]
    return obj_db


class Ball:
    def __init__(self, scr):
        """
        отвечает за создание объекта класса Ball. Создаёт шарик

        :param scr: текущий экран
        """
        self.pos = [randint(50, 1800), randint(50, 700)]
        self.color = COLOR[randint(0, 5)]
        self.angle = randint(0, 359)
        self.screen = scr
        self.speed = randint(speed_min, speed_max)
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = self.speed * sin(self.angle / 57.3)
        self.rad = randint(30, 60)
        self.score = 10

    def move(self, tic):
        """
        Отвечает за обновление координат объекта и соударения со стенками
        :param tic: текущий тик
        :return: nothing
        """
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        tic += 1
        if self.pos[0] >= 1000 - self.rad:
            self.angle = randint(90, 270)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[0] <= self.rad:
            self.angle = randint(-90, 90)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[1] >= 600 - self.rad:
            self.angle = randint(180, 360)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[1] <= self.rad:
            self.angle = randint(0, 180)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

    def draw(self):
        """
        рисует объект
        :return: nothing
        """
        circle(self.screen, self.color, self.pos, self.rad)


class Box:
    def __init__(self, scr):
        """
        Отвечает за создают объект класса Box. Создаёт квадратик
        :param scr: текущий экран
        """
        self.pos = [randint(50, 1800), randint(50, 700)]
        self.color = COLOR[randint(0, 5)]
        self.angle = randint(0, 359)
        self.screen = scr
        self.speed = randint(speed_min, speed_max)
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = self.speed * sin(self.angle / 57.3)
        self.rad = randint(30, 60)
        self.score = 20

    def move(self, tic):
        """
        Отвечает за обновление координат объекта и соударения со стенками
        :param tic: текущий тик
        :return: nothing
        """
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        if tic % fps == 0:
            self.angle = randint(0, 359)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[0] >= 1000 - self.rad:
            self.angle = randint(90, 270)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[0] <= self.rad:
            self.angle = randint(-90, 90)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[1] >= 600 - self.rad:
            self.angle = randint(180, 360)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[1] <= self.rad:
            self.angle = randint(0, 180)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

    def draw(self):
        """
        Рисует объект
        :return: nothing
        """
        a = [self.pos[0] - self.rad // (2 ** 0.5), self.pos[1] - self.rad // (2 ** 0.5),
             2 * self.rad // (2 ** 0.5), 2 * self.rad // (2 ** 0.5)]
        rect(self.screen, self.color, a)


pygame.init()
pygame.font.init()
fps = 60
screen = pygame.display.set_mode([1000, 600])
pygame.display.update()

finished = False
clock = pygame.time.Clock()
obj = []
tick = 0
score = 0
while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button = event.button
            mouse_pos = list(event.pos)
            obj = collision(obj, mouse_button, mouse_pos)

    if tick % (2 * fps) == 0:
        obj.append(Ball(screen))

    if tick % (4 * fps) == 0:
        obj.append(Box(screen))

    screen.fill(WHITE)

    for i in obj:
        i.move(tick)
        i.draw()
    font = pygame.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, (0, 0, 0))
    place = text.get_rect(center=(150, 100))
    screen.blit(text, place)

    pygame.display.update()
    tick += 1
