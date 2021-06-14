from math import sqrt
n1 = float(input('Qual o valor do cateto oposto?'))
n2 = float(input('Qual o valor do cateto adjacente?'))
cl = n1**2+n2**2
ch = sqrt(cl)
print(' O cateto oposto é:{}\n O cateto adjacente é:{}\n E o valor da hipotenusa é:{:.3f}'.format(n1, n2, ch))