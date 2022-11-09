# -*- coding: utf-8 -*-


def cos(alpha):
    print('Тут должно быть вычисление косинуса', alpha)


# оператор nonlocal
def f1():
    def f2():
        nonlocal x
        x = 27
        print('in f2 x =', x)

    x = 34
    print('in f1 x =', x)
    f2()
    print('in f1 x =', x)


x = 42
f1()
print('x =', x)
