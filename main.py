from matrix import Matrix
from tensor import Tensor

if __name__ == "__main__":
    t = Tensor(3, [1, 2, 3])
    m = Matrix(10, 10, [i for i in range(100)])
    print(m)
