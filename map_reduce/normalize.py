# 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print(L2)

