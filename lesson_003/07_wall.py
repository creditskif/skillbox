# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
brick_x, brick_y = 100, 50
row = 0
for y in range(0, sd.resolution[1], brick_y):
    row += 1
    for x in range(0, sd.resolution[0], brick_x):
        x0 = x if row % 2 else x+brick_x // 2
        point = sd.get_point(x0, y)
        point1 = sd.get_point(x0 + brick_x, y + brick_y)
        sd.rectangle(point, point1, width=1)

sd.pause()
