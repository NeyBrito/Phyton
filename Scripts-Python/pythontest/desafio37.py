n = int(input('***Informe uma das opções para conversão***\n'
              '1 para binário\n'
              '2 para octal\n'
              '3 para hexadecimal\n'))
n1 = int(input('Informe um numero para conversão: '))

if n==1:
    print(bin(n1))
if n==2:
    print(oct(n1))
if n==3:
    print(hex(n1))