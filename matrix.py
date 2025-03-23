from turtle import Turtle
from types import new_class

from tensor import Tensor


class Matrix(Tensor):
    def __init__(self, r: int, c: int, data: list):
        super().__init__((r, c), data)

    def conv_rc2i(self, r: int, c: int) -> int:
        return super().conv_coordinates2i((r, c))

    def conv_i2rc(self, i: int) -> tuple:
        return super().conv_i2coordinates(i)

    def __str__(self):
        width = max(map(len, map(str, self.data)))
        s = "[\n"
        for i in range(len(self.data)):
            s += f"{self.data[i]:>{width + 2}}"
            if (i + 1) % self.dimension[1] == 0:
                s += "\n\n"
        s = s[:-1] + "]"
        return s

    def __getitem__(self, key):
        print(type(key))
        if isinstance(key, int):
            if key < 0:
                key += self.dimension[0]
            return Matrix(1, self.dimension[1],
                          [self.data[i + key * self.dimension[1]] for i in range(self.dimension[1])])

        if isinstance(key, list):
            new_data = []
            for ind in key:
                ind %= self.dimension[0]
                new_data += self.data[ind * self.dimension[1]:(ind * self.dimension[1] + self.dimension[1])]
            return Matrix(len(key), self.dimension[1], new_data)

        if isinstance(key, slice):
            step = key.step if key.step is not None else 1
            start = key.start if key.start is not None else 0
            if step > 0:
                start %= self.dimension[0]
            stop = key.stop if key.stop is not None else self.dimension[0] * step // abs(step)
            print(start, stop, step)
            return self.__getitem__(list(range(start, stop, step)))

        if isinstance(key, tuple):
            print(key)
            print(type(key[0]))
            print(type(key[1]))
            if (isinstance(key[0], int) and isinstance(key[1], int)) is True:
                return self.data[self.conv_rc2i(key[0], key[1])]

            if isinstance(key[0], slice | list):
                new_data = []
                new_m = self.__getitem__(key[0])
                if isinstance(key[1], int):
                    for i in range(new_m.dimension[0]):
                        new_data.append(new_m[i].data[key[1]])
                elif isinstance(key[1], list):
                    for i in range(new_m.dimension[0]):
                        for j in key[1]:
                            new_data.append(new_m[i].data[j])
                else:
                    for i in range(new_m.dimension[0]):
                        new_data += new_m[i].data[key[1]]
                return Matrix(new_m.dimension[0], len(new_data) // new_m.dimension[0], new_data)


        print(type(key))
