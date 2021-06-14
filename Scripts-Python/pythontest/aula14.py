#c = 1
#while c < 11:
#    print(c, end=' ')
#    c +=1
#print('Fim')

#n = 1
#while n != 0:
#    n = int(input('Digite um valor: '))
#print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
     if n % 2 == 0:
        par += 1
     else:
        impar += 1
print('Voce digitou {} par e {} impar'.format(par, impar))