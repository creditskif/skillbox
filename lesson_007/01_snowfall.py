# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку



# class Snowflake:
#
#     def __init__(self):
#         self.color = sd.COLOR_WHITE
#         self.length = 10
#         self.speed = sd.random_number(2, 10)
#         self.x = sd.random_number(200, sd.resolution[0])
#         self.y = sd.random_number(400, sd.resolution[1])
#
#     def clear_previous_picture(self):
#         sd.clear_screen()
#
#     def __str__(self):
#         return print(f'{self.y}{self.x}')
#
#     def move(self):
#         self.y -= self.speed
#
#     def draw(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(point, self.length, self.color)
#
#     def can_fall(self):
#         if self.y > -self.length:
#             return True
#         else:
#             return False



# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
sd.background_color = sd.COLOR_BLACK
class Snowflake:

    def __init__(self):
        self.color = sd.COLOR_WHITE
        self.length = 10
        self.speed = sd.random_number(2, 10)
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.resolution[1]

    def clear_previous_picture(self):
        # sd.clear_screen()
        sd.start_drawing()
        self.color = sd.background_color
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)
        sd.finish_drawing()

    def move(self):
        self.y -= self.speed

    def draw(self):
        # point = sd.get_point(self.x, self.y)
        # sd.snowflake(point, self.length, self.color)
        sd.start_drawing()
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)
        sd.finish_drawing()

    def can_fall(self):
        if self.y > self.length:
            return True
        else:
            return False

N = 50


flake = Snowflake()
flakes_list = []
def get_fallen_flakes():
    count_fallen_flakes = 0
    for flake in flakes:
        if flake.y == 0:
            count_fallen_flakes += 1
    return count_fallen_flakes


def get_flakes(count=5):
    for i in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


def append_flakes(count):
    get_flakes(count)



flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        if flake.y > -10:
            flake.move()
        else:
            flake.y = sd.resolution[1]
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подcчитать сколько снежинок уже упало
    if fallen_flakes > 0:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0)
    if sd.user_want_exit():
        break

sd.pause()
