n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor é o maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Não existe valor maior. Os dois são iguais.')
