from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio1 = choice(lista)
sorteio2 = choice(lista)
sorteio3 = choice(lista)
sorteio4 = choice(lista)
print('A ordem de apresentação dos alunos será de:')
print('Primeiro(a) {}'.format(sorteio1))

while sorteio2 == sorteio1:
    sorteio2 = choice(lista)
print('Segundo(a) {}'.format(sorteio2))

while sorteio3 == sorteio1 or sorteio3 == sorteio2:
    sorteio3 = choice(lista)
print('Terceiro(a) {}'.format(sorteio3))

while sorteio4 == sorteio1 or sorteio4 == sorteio2 or sorteio4 == sorteio3:
    sorteio4 = choice(lista)
print('Quarto(a) {}'.format(sorteio4))