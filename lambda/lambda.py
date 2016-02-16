def build(x, y):
    return lambda: x * x + y * y


print(build(3, 4))
