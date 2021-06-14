import random
n1 = int(input('Qual numero que a máquina pensou? '))
n2 = random.randint(0,5)
if n1==n2:
    print('Você ganhou!')
else:
    print('Você perdeu!')
print('A máquina pensou no número {} e você falou o número {}!'.format(n2, n1))