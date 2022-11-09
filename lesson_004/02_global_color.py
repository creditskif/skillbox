# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 800)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
def shape(point, angle, color, length, corner):
    if angle > 360:
        return
    v1 = sd.vector(point, angle, length, color)
    # v1.draw()
    delta = 360 / corner
    next_point = v1
    next_angle = angle + delta
    shape(next_point, next_angle, color, length, corner)


point_0 = sd.get_point(300, 400)
point_1 = sd.get_point(600, 500)
point_2 = sd.get_point(100, 100)
point_3 = sd.get_point(800, 50)
angle_0 = 0
lenght_0 = 200

print("""Введите доустный цвет из существующих: 
      0: Красный
      1: Оранжевый
      2: Желтый
      3: Зеленый
      4: Cyan
      5: Синий
      6: Пурпурный      
       """)
num = input()
table_color = {
    '0': sd.COLOR_RED,
    '1': sd.COLOR_ORANGE,
    '2': sd.COLOR_YELLOW,
    '3': sd.COLOR_GREEN,
    '4': sd.COLOR_CYAN,
    '5': sd.COLOR_BLUE,
    '6': sd.COLOR_PURPLE
}

color = table_color[num]
shape(point_0, angle_0, color, lenght_0, 3)
shape(point_1, angle_0, color, lenght_0, 4)
shape(point_2, angle_0, color, lenght_0, 5)
shape(point_3, angle_0, color, lenght_0, 6)

sd.pause()
