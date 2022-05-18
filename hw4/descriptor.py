class Integer:
    def __init__(self):
        self.val = 0

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be integer')

        self.val = value


class String:
    def __init__(self):
        self.val = 0

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Must be string')

        self.val = value


class PositiveInteger:
    def __init__(self):
        self.val = 0

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be integer')

        if value < 0:
            raise ValueError('Must be positive')

        self.val = value


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price
