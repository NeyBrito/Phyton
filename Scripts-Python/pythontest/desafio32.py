#print('=== VERIFICADOR DE ANO BISSEXTO ===\n')
#ano = int(input('Qual ano a ser verificado? '))
#if ano % 400 == 0:
#print('{} é um ano bissexto.'.format(ano))
#else:
#if ano % 4 == 0:
# if ano % 100 != 0:
# print('{} é um ano bissexto.'.format(ano))
#else:
# print('{} não é um ano bissexto.'.format(ano))
#else:
#print('{} não é um ano bissexto.'.format(ano))
from datetime import date
ano = int(input('Que ano que analisar? Coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} É BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO!'.format(ano))