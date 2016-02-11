def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# print(fact(1))
#
# print(fact(5))
#
# print(fact(100))

# print(fact(5))
# print(5 * fact(4))
# print(5 * (4 * fact(3)))
# print(5 * (4 * (3 * fact(2))))
# print(5 * (4 * (3 * (2 * fact(1)))))
# print(5 * (4 * (3 * (2 * 1))))
# print(5 * (4 * (3 * 2)))
# print(5 * (4 * 6))
# print(5 * 24)
# print(120)

print(fact(1000))