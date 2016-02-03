def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        # n -= 1
        s = s * x
    return print(s)

power(5)

power(5, 2)