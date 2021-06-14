n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
#Creio que tem uma forma mais facil de fazer essa questão. Porem essa foi a mais facil que encontrei.
if n1 > n2 and n1 > n3:
    print('Maior número é: {}'.format(n1))
if n1 < n2 and n1 < n3:
    print('Menor número é: {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('Maior numero é: {}'.format(n2))
if n2 < n1 and n2 < n3:
    print('Menor número é: {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('Maior número é: {}'.format(n3))
if n3 < n1 and n3 < n2:
    print('Menor número é: {}'.format(n3))