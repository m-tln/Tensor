from matrix import Matrix
from tensor import Tensor

if __name__ == "__main__":
    t = Tensor(3, [1, 2, 3])
    m = Matrix(10, 9, [i for i in range(90)])
    print(m)
    # print(m[1, 1])
    # print(m[1])
    # print(m[-1])
    # print(m[1:4])
    # print(m[:4])
    # print(m[4:])
    # print(m[:])
    # print(m[1:7:2])
    # print(m[:, 1])
    # print(m[1:4, 1:4])
    # print(m[1:4, :4])
    # print(m[1:4, 4:])
    # print(m[1:4, :])
    # print(m[-1:])
    # print(m[-2::-2])
    # print(m[-2::-2, 1:4])
    # print(m[:, :])
    # print(m[[1, 4]])
    # print(m[:, [1, 4]])
    print(m[[1, 4], [1, 4]])




