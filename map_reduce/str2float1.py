from functools import reduce


def str2float(s):
    float = len(s) - s.index('.') - 1
    s = s.replace('.', '')

    def chr2num(m):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[m]

    def order(a, b):
        return a * 10 + b

    return reduce(order, map(chr2num, s)) / 10 ** float


print('str2float(\'123.456\')=', str2float('123.456'))
