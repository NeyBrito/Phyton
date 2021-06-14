from random import randint
pc = randint(0, 10)
print('Sou seu computador. Acabei de pensar em numer em um número de 0,10. \n Será que você acerta?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} palpites.'.format(palpites))
