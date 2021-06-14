import datetime
an = int(input('Qual seu ano de nascimento? '))
a = datetime.date.today().year
ca = a - an
fp = 18 - ca
if ca == 18:
    print('Você está na idáde de alistamento. Vá na junta militar de sua cidade.')
elif fp == 0:
    print('Vá a junta militar se sua cidade imediatamente.')
elif ca < 18:
    print('Você ainda não está na idáde de alistamento. Faltam {} para seu alistamento.'.format(fp))
elif ca > 18:
    print('Você já passou da idáde de alistamento. Passaram-se {} ano(s) da data de alistamento.'.format(fp))
