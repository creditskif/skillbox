# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.soviet_street.house1 import room1 as s_h1_r1
from district.soviet_street.house1 import room2 as s_h1_r2

from district.soviet_street.house2 import room1 as s_h2_r1
from district.soviet_street.house2 import room2 as s_h2_r2

from district.central_street.house1 import room1 as s_h3_r1
from district.central_street.house1 import room2 as s_h3_r2

from district.central_street.house2 import room1 as s_h4_r1
from district.central_street.house2 import room2 as s_h4_r2


people = s_h1_r1.folks + s_h1_r2.folks + s_h2_r1.folks + s_h2_r2.folks + s_h3_r1.folks + s_h3_r2.folks + s_h4_r1.folks + s_h4_r2.folks
print("На районе живут", ',\n '.join(people ))



