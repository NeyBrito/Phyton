print('-='*20)
print(' \033[33m''Simulador de Empréstimos!''\033[m')
print('-='*20)
nome = str(input('Qual o seu nome senhor? '))
vc = float(input('Qual o valor da casa senhor? '))
sl = float(input('Qual o seu salário senhor? '))
ap = float(input('Em quantos anos pretende pagar? '))
ms = ap*12
vp = vc/(ap*12)
if vc/(ap*12) > (30/100)*sl:
    print('Desculpe senhor! Seu empréstimo foi negado.')
elif vc/(ap*12) < (30/100)*sl:
    print('Seu emprestimo foi aprovado senhor!\n A parcela será de R${:.2f} em {:.2f} mêses.'.format(vp, ms))
print('*'*20)
print('Tenha um Bom dia, Senhor!')
print('*'*20)