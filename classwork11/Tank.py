from math import cos, sin, atan
from random import randint
import pygame
import numpy as np
from screeninfo import get_monitors
from pygame.draw import *
from pygame.font import *
from copy import deepcopy


def get_res():
    """
    Получает разрешение вашего монитора
    Возвращает кортеж с разрешением,
    выводит параметры вашего монитора на экран
    """
    monitor = str(get_monitors()[0])[8:-1].split(', ')
    current_resolution = (int(monitor[2][6:]), int(monitor[3][7:]))
    print('Your screen resolution is', current_resolution[0], 'x', current_resolution[1])
    return current_resolution

def collision(a, b):

    t = False
    for j in range(len(b) - 1, -1, -1):
        l = ((a.pos[0] - b[j].pos[0]) ** 2 + (a.pos[1] - b[j].pos[1]) ** 2) ** 0.5
        if l <= a.radius + b[j].radius:
            global score
            score += b[j].score
            del b[j]
            t = True
    return b, t

res = get_res()
fps = 60
pygame.init()

m_color = (60, 60, 60)
s_color = (20, 20, 20)
g_color = (100, 100, 100)


class Tank:
    def __init__(self, current_scr):
        self.scr = current_scr
        self.pos = np.array([res[0]//2, res[1]-50])
        self.speed = 0
        self.hp = 3
        self.power = 0
        self.gun_angle = 0
        self.gun_pos = np.array([0, 0])
        self.scl = 1

    def aiming(self):
        len1 = mouse_pos[0] - self.pos[0]
        len2 = mouse_pos[1] - self.pos[1]
        if (mouse_pos[1] > res[1] - 110) and (mouse_pos[0] > self.pos[0]):
            self.gun_angle = 0
        elif (mouse_pos[1] > res[1] - 110) and (mouse_pos[0] < self.pos[0]):
            self.gun_angle = 180
        elif len1 == 0:
            self.gun_angle = 0
        else:
            self.gun_angle = atan(len1/len2) * 57.3 + 90

    def draw(self):
        circle(self.scr, g_color, self.pos, 25 * self.scl)
        cord1 = np.array([[100, 0], [80, 40], [-80, 40], [-100, 0]]) * self.scl
        otn_arr4 = np.array([[self.pos[0], self.pos[1]] * 4]).reshape(4, 2)
        polygon(self.scr, m_color, cord1 + otn_arr4)
        self.gun()

    def shoot(self):
        global bullet_db
        bullet_db.append(Bullet(self.gun_pos, self.power, self.gun_angle, self.scr))

    def gun(self):
            '''
            Отвечает за рисовку самой пушки танка и рассчёт её координат после поворота


            '''
            an = self.gun_angle / 57.3
            power_shoot = self.power
            cx = self.pos[0]
            cy = self.pos[1]
            otn_arr2 = np.array([[cx, cy] * 2]).reshape(2, 2)
            otn_arr4 = np.array([[cx, cy] * 4]).reshape(4, 2)

            gun_l_b = 20
            gun_l_mi = 70
            gun_l_ma = 150
            gun_r = 5

            gun_l = gun_l_mi + (gun_l_ma - gun_l_mi) * power_shoot / 100
            coord_shar = np.array([0, 0])
            otn_coord_shar = np.array([coord_shar] * 4).reshape(4, 2)
            otn_coord_shar2 = np.array([coord_shar] * 2).reshape(2, 2)

            coord_gun = np.array([[-gun_l_b * cos(an) + gun_r * sin(an), gun_l_b * sin(an) + gun_r * cos(an)],
                                  [-gun_l_b * cos(an) - gun_r * sin(an), gun_l_b * sin(an) - gun_r * cos(an)],
                                  [gun_l * cos(an) - gun_r * sin(an), -gun_l * sin(an) - gun_r * cos(an)],
                                  [gun_l * cos(an) + gun_r * sin(an), -gun_l * sin(an) + gun_r * cos(an)]])

            coord_gun_start_bul = np.array([[gun_l * cos(an), -gun_l * sin(an)],
                                            [gun_l * cos(an), -gun_l * sin(an)]])

            coord_gun_it = ((coord_gun + otn_coord_shar) * self.scl + otn_arr4).astype(int)

            coord_gun_start_bul_it = ((coord_gun_start_bul + otn_coord_shar2) * self.scl + otn_arr2).astype(int)

            polygon(self.scr, m_color, coord_gun_it)
            aalines(self.scr, m_color, True, coord_gun_it)

            self.gun_pos = coord_gun_start_bul_it[0]

    def move(self):
        self.pos[0] += self.speed
        if self.pos[0] <= 100:
            self.pos[0] = 100
        elif self.pos[0] >= res[0] - 100:
            self.pos[0] = res[0] - 100
class Bullet:
    def __init__(self, pos, power, ang, scr,):
        max_speed = 100
        self.pos = pos
        self.speed = power * max_speed // 100
        self.angle = ang
        self.radius = 5
        self.scr = scr
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = -self.speed * sin(self.angle / 57.3)

    def draw(self):
        circle(self.scr, (255, 0, 0), self.pos, self.radius)

    def move(self):
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        self.speed_y += gravity


class Target:
    def __init__(self, scr):
        max_speed = 5
        self.pos = np.array([randint(100, res[0] - 100), randint(100, res[1] - 100)])
        self.radius = randint(20, 50)
        self.speed = randint(50, 100) / 100 * max_speed
        self.angle = randint(0, 359)
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = - self.speed * sin(self.angle / 57.3)
        self.scr = scr
        self.score = 5

    def move(self):
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        if self.pos[0] < self.radius:
            self.speed_x = -self.speed_x
            self.pos[0] = self.radius
        if self.pos[0] > res[0] - self.radius:
            self.speed_x = -self.speed_x
            self.pos[0] = res[0] - self.radius
        if self.pos[1] < self.radius:
            self.speed_y = -self.speed_y
            self.pos[1] = self.radius
        if self.pos[1] > res[1] - self.radius - 200:
            self.speed_y = -self.speed_y
            self.pos[1] = res[1] - self.radius - 200

    def draw(self):
        circle(self.scr, (0, 0, 0), self.pos, self.radius)
        circle(self.scr, (255, 0, 0), self.pos, self.radius // 2)


class Enemy:
    def __init__(self, scr):
        self.surf = pygame.image.load("bear.jpg")
        self.scr = scr
        self.speed = randint(-2, 2)
        self.radius = 50
        self.pos = np.array([randint(100, res[0] - 100), randint(100, res[1] - 100)])
        self.score = 10

    def move(self):
        self.pos[0] += self.speed
        if self.pos[0] <= self.radius:
            self.speed = -self.speed
            self.pos[0] = self.radius

        elif self.pos[0] >= res[0] - self.radius:
            self.speed = -self.speed
            self.pos[0] = self.pos[0] - self.radius

    def attack(self):
        bomb_db.append(Bomb(self.scr, self.pos, self.speed))

    def draw(self):
        self.scr.blit(self.surf, self.pos - np.array([50, 50]))


class Bomb:
    def __init__(self, scr, pos, speed_x):
        self.scr = scr
        self.pos = deepcopy(pos)
        self.speed_y = 0
        self.speed_x = speed_x
        self.radius = 10

    def move(self, i):
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        self.speed_y += gravity
        if self.pos[0] < 0:
            self.pos[0] = 0
            self.speed_x = -self.speed_x

        elif self.pos[0] > res[0]:
            self.pos[0] = res[0]
            self.speed_x = -self.speed_x

        if self.pos[1] >= res[1] - 50:
            global tunk, bomb_db
            if (self.pos[0] >= tunk.pos[0] - 100) and (self.pos[0] <= tunk.pos[0] + 100):
                tunk.hp -= 1

            del bomb_db[i]

    def draw(self):
        circle(self.scr, (70, 70, 70), self.pos, self.radius)




screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
finished = False
charging = False
tick = 0
tunk = Tank(screen)
mouse_pos = np.array((0, 0))
bullet_db = []
enemy_db = []
target_db = []
bomb_db = []
gravity = 1
tank_max_speed = 5
score = 0
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                finished = True
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            tunk.aiming()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            charging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            charging = False
            tunk.shoot()
            tunk.power = 0

    keys = pygame.key.get_pressed()
    if keys[100] and keys[97]:
        tunk.speed = 0
    elif keys[100]:
        tunk.speed = tank_max_speed
    elif keys[97]:
        tunk.speed = -tank_max_speed
    else:
        tunk.speed = 0
        
    if tunk.hp <= 0:
        finished = True
        print("You died")
    tunk.move()
    
    for i in range(len(target_db) - 1, -1, -1):
        target_db[i].move()
    for i in range(len(enemy_db) - 1, -1, -1):
        enemy_db[i].move()
    for i in range(len(bomb_db) - 1, -1, -1):
        bomb_db[i].move(i)
    for i in range(len(bullet_db) - 1, -1, -1):
        bullet_db[i].move()
    
    for i in range(len(bullet_db) - 1, -1, -1):
        target_db, t = collision(bullet_db[i], target_db)
        if t:
            del bullet_db[i]
    for i in range(len(bullet_db) - 1, -1, -1):
        enemy_db, t = collision(bullet_db[i], enemy_db)
        if t:
            del bullet_db[i]
    
    if tick % (fps * 1) == 0:
        target_db.append(Target(screen))
    if tick % (fps * 2) == 0:
        enemy_db.append(Enemy(screen))
    if tick % (fps * 5) == 0:
        for i in enemy_db:
            i.attack()

    for i in range(len(target_db) - 1, -1, -1):
        target_db[i].draw()
    for i in range(len(enemy_db) - 1, -1, -1):
        enemy_db[i].draw()
    for i in range(len(bomb_db) - 1, -1, -1):
        bomb_db[i].draw()
    for i in range(len(bullet_db) - 1, -1, -1):
        bullet_db[i].draw()

    font = pygame.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, (0, 100, 255))
    place = text.get_rect(center=(150, 100))
    screen.blit(text, place)

    font = pygame.font.Font(None, 40)
    text = font.render("HP:" + str(tunk.hp), True, (255, 0, 0))
    place = text.get_rect(center=(150, 150))
    screen.blit(text, place)

    if charging:
        tunk.power += 1

    clock.tick(fps)
    tunk.draw()
    pygame.display.update()
    tick += 1
    screen.fill((255, 255, 255))