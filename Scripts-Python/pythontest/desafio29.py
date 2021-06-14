ca = float(input('Qual sua velocidade?'))
if ca > 80:
    n1 = (ca - 80) * 7
    print(' Você está acima do limite de velocidade. REDUZA!\n Você está sendo multado em {:.2f}'.format(n1))
else:
    print('Você está dentro do limite de velocidade. BOA VIAGEM!')

