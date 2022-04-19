class CustomList(list):

    def __add__(self, other):
        new_len = max(len(self), len(other))
        new_list = CustomList([0]*new_len)

        for i, val in enumerate(self):
            new_list[i] += val
        for i, val in enumerate(other):
            new_list[i] += val

        return new_list

    __radd__ = __add__

    def __neg__(self):
        return CustomList(-i for i in self)

    def __sub__(self, other):
        return -(-self + other)

    def __rsub__(self, other):
        return -self + other

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return f'{list(self)}, {sum(self)}'
