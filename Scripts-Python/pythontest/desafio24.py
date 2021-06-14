frase = str(input('Digite um nome de uma cidade:'))
dividido = frase.split()
print('Tem SANTO no primeiro noma da cidade {}:'.format(frase), 'SANTO' in dividido[0])