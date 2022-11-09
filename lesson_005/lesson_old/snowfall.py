# -*- coding: utf-8 -*-
import random

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

sd.resolution = (1200, 600)
x, y, z = [], [], []
ys, yy, xx = [], [], []
y_minus, x_minus, index = 0, 0, 0
light = 50
step = 10
N = 30
for _ in range(N):
    i = sd.random_number(0, 1100)
    j = sd.random_number(600, 1000)
    k = sd.random_number(10, 40)
    x.append(i)
    y.append(j)
    z.append(k)
    yy.append(0)
    ys.append(0)
    xx.append(0)

while True:
    sd.clear_screen()
    for i in range(N):
        if y[i] + yy[i] < -light:
            yy[i] = 0
        new_y = y[i] + yy[i]
        new_x = x[i] + x_minus
        point = sd.get_point(new_x, new_y)
        sd.snowflake(point, z[i])
        x_minus = sd.random_number(10, 20)

    for i in range(N):
        yy[i] -= step
        if ys[i] + y[i] > 0:
            ys[i] -= step

    y_minus -= step
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


