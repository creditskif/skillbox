# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None


    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)
    def go_to_the_house(self, house):
        self.house = house
        self.house.cat = True
        self.fullness -= 10
        cprint(f'{self.name} въехал в дом', color='cyan')


# Когда кот спит - сытость уменьшается на 10
    def sleep_cat(self):
        self.fullness -= 10
        cprint('{} поспал' .format(self.name), color='red')

    # Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')


# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
    def tear_wallpeper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('{} дерет обои'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_wallpeper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep_cat()

class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.zp = 50

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def work(self, zp):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += zp
        self.fullness -= 10

    def salary_increase(self, zp):
        cprint('{} подняли зп'.format(self.name), color='blue')
        self.zp += 100

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_man += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat(self):
        if self.house.cat:
            if self.house.money >= 50:
                cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
                self.house.money -= 50
                self.house.food_cat += 50
            else:
                cprint('{} деньги кончились!'.format(self.name), color='red')
        else:
            print('У {} нет кота'.format(self.name))


    def eat(self):
        if self.house.food_man >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food_man -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.shopping()

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def cleaning_the_house(self): #   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
        if self.house.mud >= 5:
            if self.house.mud < 100:
                self.house.mud = 0
            else:
                self.house.mud -= 100
            self.fullness -= 20
            cprint('{} убрался в доме'.format(self.name), color='green')
        else:
            cprint('{} в доме убираться не нужно'.format(self.name), color='green')

    def pick_up_a_cat(self, cat):
        cat.house = self.house
        cprint(f'{self.name} подобрал {cat.name}', color='white')


    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 8)
        if self.fullness < 25:
            self.eat()
        elif self.house.food_man < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work(zp=self.zp)
        elif self.house.food_cat < 10:
            self.shopping_cat()
        elif self.house.mud > 0:
            self.cleaning_the_house()
        elif dice == 1:
            self.work(zp=self.zp)
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.shopping_cat()
        elif dice == 4:
            self.cleaning_the_house()
        elif dice == 5:
            if self.zp != 150:
                self.salary_increase(zp=self.zp)
            self.work(zp=self.zp)
        else:
            self.watch_MTV()

class House:
    def __init__(self):
        self.food_man = 50
        self.food_cat = 0
        self.money = 0
        self.mud = 0
        self.cat = None


    def __str__(self):
        return "В доме осталось- Еды: для человека = " + str(self.food_man) +" для кота = "+ str(self.food_cat) + \
               " , Денег = " + str(self.money) + ". Загрязненность комнаты = " + str(self.mud)

citizens = [
    Man(name='Влад'),
]
cats = [
    Cat(name='Барсик'),
    Cat(name='Торчёк'),
]

for citizens_cats in cats:
    citizens[0].pick_up_a_cat(cat=citizens_cats)
    citizens.append(citizens_cats)

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
