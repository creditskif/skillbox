# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
x_0 = 50
y_0 = 50
x_end = 350
y_end = 450
point_0 = sd.get_point(x_0, y_0)
point_end = sd.get_point(x_end, y_end)
# for i in range(7):
#     sd.line(point_0, point_end, rainbow_colors[i], 4)
#     x_0 += 5
#     x_end += 5
#     point_0 = sd.get_point(x_0, y_0)
#     point_end = sd.get_point(x_end, y_end)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

x = 300
y = -200
point = sd.get_point(x, y)
r = 500
width = 30
for i in range(7):
    sd.circle(point, r, rainbow_colors[i], width)
    r += width
sd.pause()
