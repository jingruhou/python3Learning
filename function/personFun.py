def person(name, age, **kw):
    print('name:', name, 'age', age, 'other:', kw)

print(person('Michael', 30))

print(person('Bob', 35, city='Beijing'))

print(person('Adam', 45, gender='M', job='Engineer'))

extra0 = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 25, city=extra0['city'], job=extra0['job']))

extra1 = {'city': 'Beijing', 'job': 'Enginer'}
print(person('Jack', 24, **extra1))