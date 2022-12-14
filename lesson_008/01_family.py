# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме денег: {self.money}, еды: {self.food}, еда_кота: {self.cat_food} грязи: {self.dirt}'


class Human:
    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def __str__(self):
        return f'еда: {self.fullness}, счастье {self.happiness}'

    def eat(self):
        eat_now = randint(0, 30)
        self.fullness += eat_now
        self.house.food -= eat_now
        print("{} покушал.".format(self.name))

    def depression(self):
        if self.house.dirt >= 90:
            self.happiness -= 5

    def patting_the_cat(self):
        self.happiness += 5
        print("{} погладил кота".format(self.name))


class Husband(Human):
    rate_fullness = 10

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):
        if self.fullness < 0:
            print("{} умер от голода".format(self.name))
            return
        if self.happiness < 10:
            print("{} умер от депрессии".format(self.name))
            return
        super().depression()
        dice = randint(1, 4)
        if self.fullness < 10:
            self.eat()
        elif self.house.money < 100:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            super().patting_the_cat()
        else:
            self.gaming()

    def work(self):
        self.fullness -= Husband.rate_fullness
        self.house.money += 150
        print("{} сходил на работу.".format(self.name))

    def gaming(self):
        self.fullness -= Husband.rate_fullness
        self.happiness += 20
        print("{} поиграл в Танки.".format(self.name))


class Wife(Human):
    rate_fullness = 10

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):
        dice = randint(1, 4)
        if self.fullness < 0:
            print("{} умерла от голода".format(self.name))
            return
        if self.happiness < 10:
            print("{} умерла от депрессии".format(self.name))
            return
        super().depression()
        if self.fullness < 10:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.happiness < 20:
            self.buy_fur_coat()
        elif dice == 1:
            self.buy_fur_coat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            super().patting_the_cat()
        else:
            self.shopping()

    def shopping(self):
        if self.house.money > 30:
            self.fullness -= Wife.rate_fullness
            self.house.food += 30
            self.house.money -= 60
            self.house.cat_food += 30
            print("{} сходила в магазин за продуктами".format(self.name))
        else:
            print("У {} нет денег ".format(self.name))

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.house.money -= 350
            self.fullness -= Wife.rate_fullness
            self.happiness += 60
            print("{} купила шубу".format(self.name))
        else:
            print("У {} не хватает денег на шубу".format(self.name))

    def clean_house(self):
        self.fullness -= Wife.rate_fullness
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        print("{} убралась в доме".format(self.name))


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#     home.dirt += 5
#
# # TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    def __init__(self, name):
        super().__init__()
        self.house = home
        self.name = name
        self.fullness = 30

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}'

    def act(self):
        if self.fullness < 0:
            print('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        eating = randint(1, 10)
        self.fullness += 2 * eating
        self.house.cat_food -= eating
        print("{} покушал".format(self.name))
    def sleep(self):
        self.fullness -= 10
        print("{} спит".format(self.name))

    def soil(self):
        self.house.dirt += 5
        self.fullness -= 10
        print('{} дерет обои'.format(self.name))

# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# cat = Cat(name='Барсик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cat.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(cat, color='cyan')
#     cprint(home, color='cyan')
#     home.dirt += 5
#
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
class Child():
    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = home
        self.happiness = 100

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):
        if self.fullness < 0:
            print("{} умер....".format(self.name))
        dict =randint(1,3)
        if self.fullness < 10:
            self.eat()
        elif dict == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.house.food -= 10
        print('{} покушал'.format(self.name))

    def sleep(self):
        print('{} поспал'.format(self.name))

#
# # TODO после реализации второй части - отдать на проверку учителем две ветки
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat = Cat(name='Барсик')
child = Child(name='Пупсик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cat.act()
    child.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(cat, color='cyan')
    cprint(child, color='cyan')
    cprint(home, color='cyan')
    home.dirt += 5
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#
