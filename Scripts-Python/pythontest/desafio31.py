km = float(input('Qual a distância da sua viagem em Km? '))
if km <= 200:
    pr1 = km*0.50
    print('Você vai pagar na sua viagem: {:.2f}'.format(pr1))
else:
    pr2 = km*0.45
    print('Você irá gasta na sua viagem: {:.2f}'.format(pr2))
print('Boa Viagem!')