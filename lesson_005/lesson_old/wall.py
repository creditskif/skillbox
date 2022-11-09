# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1200,600)
# TODO здесь ваш код
def brick(x_0, y_0, x_end, y_end):
    for y in range(y_0, y_end, 50):
        y1 = y + 50
        if y % 100 == 0:
            x_0 += 50
        else:
            x_0 -= 50
        for x in range(x_0, x_end, 100):
            x1 = x + 100
            point = sd.get_point(x, y)
            point1 = sd.get_point(x1, y1)
            sd.rectangle(point, point1, width=1)

# brick(300, 100, 900, 300)
# sd.pause()
