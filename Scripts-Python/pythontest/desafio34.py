s1 = float(input('Qual o sálario a ser alterado? '))
am1 = ((10/100)*s1)+s1
am2 = ((15/100)*s1)+s1
if s1 >= 1250:
    print('Esse salário está hábil a receber um aumento de 10% passando a ser: {}'.format(am1))
else:
    print('Esse salário está hábil a receber um aumento de 15% passando a ser: {}'.format(am2))