class Pet:
    """ Домашнее животное """


    def __init__(self, name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__, self.name)  # ссылка на класс обьекта и далее на имя класса
        print('  Всего ног:', self.legs)
        print('  Хвост присутствует -', 'да' if self.has_tail else 'нет')
        print(self.__dict__)  # подкапотный словарь атрибутов и методов


pet = Pet(name="Кузя")
pet.inspect()
print(pet.__class__ is Pet)