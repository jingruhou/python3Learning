name = ['Adam', 'Alex', 'Amy', 'Bob', 'Boom', 'Candy', 'Chris', 'David', 'Jason', 'Jasonstatham', 'BIll']

i_name = input('please input name:').title()

wname = []

for n in name:
    if n[0:len(i_name)] == i_name:
        wname.append(n)

if len(wname) != 0:
    print('Do you want to find %s?'%(wname))
else:
    print('%s not find'%(i_name))