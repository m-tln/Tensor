from tensor import Tensor


class Matrix(Tensor):
    def __init__(self, r : int, c : int, data: list):
        super().__init__((c, r), data)

    def conv_rc2i(self, r: int, c: int) -> int:
        return super().conv_coordinates2i((r, c))

    def conv_i2rc(self, i : int) -> tuple:
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