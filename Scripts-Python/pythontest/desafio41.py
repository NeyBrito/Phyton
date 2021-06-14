from pickletools import i

print('{}'.format(i))
if i <= 9:
    print('Categoria {}MIRIM{}!'.format('\033[1;7;30m', '\033[m'))
elif i > 9 and i <=14:
    print('Categoria {}INFANTIL{}!'.format('\033[1;7;30m', '\033[m'))
elif i > 14 and i <=19:
    print("Categoria {}JUNIOR{}!".format('\033[1;7;30m', '\033[m'))
elif i > 19 and i <=20:
    print("Categoria {}Master{}!".format('\033[1;7;30m', '\033[m'))
