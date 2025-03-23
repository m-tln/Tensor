class Tensor:
    def __init__(self, dimension: int | tuple, data: list):
        self.dimension = dimension
        self.data = data

    def __str__(self):
        return str(self.data)