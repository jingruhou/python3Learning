def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)


print(person('Jack', 24, city='Kunming', adr='Chenggong', zipcode=547688))
