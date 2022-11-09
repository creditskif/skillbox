# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# TODO здесь ваш код
# for good in goods:
#     code_goods = goods[good]
#     total_price = 0
#     total_quantity = 0
#     for quntity_price in store[code_goods]:
#         total_price = total_price + quntity_price['quantity'] * quntity_price['price']
#         total_quantity += quntity_price['quantity']
#     print(good, '-', total_quantity, 'шт, стоимость ', total_price, 'руб')

zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0
for animal in zoo_pet_mass:
    mass = zoo_pet_mass[animal]
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)
