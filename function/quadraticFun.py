# 定义一个函数quadratic(a, b, c)，
# 接收3个参数，返回一元二次方程：
# ax*x + bx + c = 0的两个解

# ax²+bx+c=0(a≠0)
# Δ=b²-4ac
# ①若Δ=b²-4ac＜0
# 则无实数根
# ②若Δ=b²-4ac=0
# 则有两个相等的实数根（即就一个）
# x=-b/2a
# ③若Δ=b²-4ac＞0
# 则有两个不相等的实数根
# x1=[-b-√(b²-4ac)]/2a
# x2=[-b+√(b²-4ac)]/2a

import math


def quadratic(a, b, c):
    if a != 0:
        delta = b * b - 4 * a * c
        if delta < 0:
            print('no result !')
        elif delta == 0:
            print('two equal result !')
            x = -b/2*a
            return print('x1=x2=', x)
        elif delta > 0:
            # x1=[-b - √(b*b-4*a*c)] / 2*a
            # x2=[-b + √(b*b-4*a*c)] / 2*a
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print('two result !')
            return x1, x2
    else:
        x = -c / b
        return x


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))