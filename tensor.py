class Tensor:
    def __init__(self, dimension: int | tuple, data: list):
        self.dimension = dimension
        self.data = data

    def __str__(self):
        return str(self.data)

    def conv_coordinates2i(self, coordinates: tuple | int) -> int:
        if isinstance(coordinates, int) != isinstance(self.dimension, int):
            raise ValueError("Invalid coordinates dim")
        elif isinstance(coordinates, tuple) and (len(coordinates) != len(self.dimension)):
            raise ValueError("Invalid coordinates dim")
        elif isinstance(coordinates, int):
            return coordinates

        mul = 1
        for d in self.dimension:
            mul *= d

        res = 0
        for i in range(len(coordinates) - 1, -1, -1):
            mul //= self.dimension[i]
            res += mul * coordinates[i]

        return res

    def conv_i2coordinates(self, i: int) -> tuple | int:
        if isinstance(self.dimension, int):
            return i

        mul = 1
        for d in self.dimension:
            mul *= d

        coordinates = []
        for d in self.dimension[::-1]:
            mul //= d
            coordinates.append(i // mul)
            i %= mul

        return (coordinates[::-1],)
