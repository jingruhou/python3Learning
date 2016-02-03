def person(name, age, *, city='Kunming', job):
    print(name, age, city, job)


person('Jack', 26, job='Engineer')
