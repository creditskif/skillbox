# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
#Water, Air, Fire, Earth, Storm, Steam, Mud, Lightning, Dust, Lava.
class Water:
    def __init__(self):
        self.name = "Вода"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Stream(part1=self, part2=other)
        elif isinstance(other,Earth):
            return Mud(part1=self, part2=other)
        else:
            return None

class Air:
    def __init__(self):
        self.name = "Воздух"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lighthing(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        else:
            return None

class Fire:
    def __init__(self):
        self.name = "Огонь"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava(part1=self, part2=other)
        else:
            return None

class Earth:
    def __init__(self):
        self.name = "Земля"


    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Mud(part1=self, part2=other)
class Storm:
    def __init__(self, part1, part2):
        self.name = "Шторм"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

class Stream:
    def __init__(self, part1, part2):
        self.name = "Пар"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

class Mud:
    def __init__(self, part1, part2):
        self.name = "Грязь"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

class Lighthing:
    def __init__(self, part1, part2):
        self.name = "Молния"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

class Dust:
    def __init__(self, part1, part2):
        self.name = "Пыль"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

class Lava:
    def __init__(self, part1, part2):
        self.name = "Лава"
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + " = " + str(self.name)

result = Water() + Air()
print(result)
result = Water() + Fire()
print(result)
result = Water() + Earth()
print(result)
result = Air() + Fire()
print(result)
result = Air() + Earth()
print(result)
result = Fire() + Earth()
print(result)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
