# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# TODO здесь ваш код
result, tmp = 0, a
while tmp > b:
    tmp = tmp - b
    result += 1
print('Целочисленное деление', a, 'на', b, 'даёт', result)