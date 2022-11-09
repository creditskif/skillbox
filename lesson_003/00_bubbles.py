# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rnd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
center = sd.Point(650, 300)
sd.circle(center, 50)
sd.circle(center, 45)
sd.circle(center, 40)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, radius, step, color):
    sd_point = sd.Point(*point)
    sd.circle(sd_point, radius, color)
    sd.circle(sd_point, radius - step, color)
    sd.circle(sd_point, radius - 2 * step, color)

#
# # Нарисовать 10 пузырьков в ряд
# # TODO здесь ваш код
# first_point = (100, 100)
# color = (255, 255, 255)
# delta = 100
# radius = 30
# step = 5
# for number in range(10):
#     point = (first_point[0] + number * delta, first_point[1])
#     bubble(point, radius, step)
# j = 0
# # Нарисовать три ряда по 10 пузырьков
# # TODO здесь ваш код
# for number in range(10):
#     for i in range(3):
#         point = (first_point[0] + number * delta, first_point[1] + j)
#         bubble(point, radius, step)
#         j = j + 100
#     j = 0
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range(100):
    bubble((rnd.randint(10,1290), rnd.randint(10,590)), 20, 5,
           (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)))

sd.pause()
