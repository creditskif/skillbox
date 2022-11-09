# -*- coding: utf-8 -*-

import simple_draw as sd
import random
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
sd.resolution = (900, 800)

def draw_bunches(start_point, angle, length):
    if length < 6:
        return
    v1 = sd.get_vector(start_point, angle, length)
    v1.draw()
    next_point = v1.end_point
    rand_angle = random.randint(20, 35)
    rand_lenght = random.uniform(0.70, 0.75)
    next_angel = angle + rand_angle
    next_angel1 = angle - rand_angle
    next_length = length * rand_lenght
    draw_bunches(next_point, next_angel, next_length)
    draw_bunches(next_point, next_angel1, next_length)


root_point = sd.get_point(450, 30)
draw_bunches(start_point=root_point, angle=90, length=200)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


