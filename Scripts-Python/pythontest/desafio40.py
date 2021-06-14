nt1 = float(input('Nota primeira prova: '))
nt2 = float(input('Nota segunda prova: '))
md = (nt1+nt2)/2
if md < 5.0:
    print(' Sua média é: {}\n REPROVADO!'.format(md))
elif md >= 5.0 and md <= 6.9:
    print(' Sua média é: {}\n RECUPERAÇÃO!'.format(md))
elif md >= 7.0:
    print(' Sua média é: {}\n APROVADO!'.format(md))
