from functools import reduce


def prod(L):
    def mult(x, y):
        return x * y

    return reduce(mult, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
