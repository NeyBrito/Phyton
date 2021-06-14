print ('======Calculador de Triângulos======')
r1 = float(input('Tamanho da primeira reta: '))
r2 = float(input('Tamanho da segunda reta: '))
r3 = float(input('Tamanho da terceira reta: '))

if (r2 - r3)< r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2)< r3 < r1 + r2:
    print('Estas retas formam um triângulo!')
else:
    print('Essas retas não formam um triângulo!')
