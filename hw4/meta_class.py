class CustomMeta(type):

    def __new__(mcs, name, bases, dct):
        custom_attrs = {
            name if name.startswith('__') else 'custom_' + name: value
            for name, value in dct.items()
        }
        return type.__new__(mcs, name, bases, custom_attrs)

    def custom_setattr(cls, key, val):
        cls.__dict__['custom_' + key] = val

    def __call__(cls, *args, **kwargs):
        cls.__setattr__ = CustomMeta.custom_setattr

        self = type.__call__(cls, *args, **kwargs)
        custom_dict = {}
        for key, val in self.__dict__.items():
            custom_dict['custom_' + key] = val
        self.__dict__ = custom_dict

        return self


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
