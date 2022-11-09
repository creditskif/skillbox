# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
# print("""Возможные фигуры:
#       0: Треугольник
#       1: Квадрат
#       2: Пятиугольник
#       3: Шестиугольник
#        """)
# num = input()
sd.resolution = (1200, 600)


def shape(point, angle, color, length, corner):
    if angle > 360:
        return
    v1 = sd.vector(point, angle, length, color)
    # v1.draw()
    delta = 360 / corner
    next_point = v1
    next_angle = angle + delta
    shape(next_point, next_angle, color, length, corner)


point_0 = sd.get_point(500, 150)
point_1 = sd.get_point(600, 500)
point_2 = sd.get_point(100, 100)
point_3 = sd.get_point(800, 50)
angle_0 = 0
lenght_0 = 200
color_0 = sd.COLOR_RED

while True:
    num = input("""Возможные фигуры: 
      0: Треугольник    
      1: Квадрат
      2: Пятиугольник
      3: Шестиугольник   
       """)
    if not num.isnumeric():
        print("Вы ввели не число. Попробуйте снова: ")
    elif not 0 <= int(num) <= 3:
        print("Ваше число не диапазоне. Попробуйте снова")
    else:
        break

if num == '0':
    shape(point_0, angle_0, color_0, lenght_0, 3)
if num == '1':
    shape(point_0, angle_0, color_0, lenght_0, 4)
if num == '2':
    shape(point_0, angle_0, color_0, lenght_0, 5)
if num == '3':
    shape(point_0, angle_0, color_0, lenght_0, 6)

sd.pause()
