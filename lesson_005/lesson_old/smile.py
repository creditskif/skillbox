# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш ко
r = 50
point_list = []


def smily(x0=0, y0=0, r=50, n=10, rand=0):
    for _ in range(n):
        if rand == 0:
            x = sd.random_number(0, 600)
            y = sd.random_number(0, 600)
        else:
            x, y = x0, y0
        point = sd.get_point(x, y)
        sd.circle(point, r)
        point = sd.get_point(x + r / 3, y + r / 3)
        sd.circle(point, radius=5)
        point = sd.get_point(x - r / 3, y + r / 3)
        sd.circle(point, radius=5)
        point_list.append(sd.get_point(x - r / 2, y - r / 3))
        point_list.append(sd.get_point(x - r / 4, y - r / 2))
        point_list.append(sd.get_point(x + r / 4, y - r / 2))
        point_list.append(sd.get_point(x + r / 2, y - r / 3))
        sd.lines(point_list)
        point_list.clear()

# smily()
# sd.pause()
