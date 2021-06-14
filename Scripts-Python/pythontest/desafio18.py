import math
a1 = float(input('Digite um angulo:'))
s = math.sin(math.radians(a1))
c = math.cos(math.radians(a1))
t = math.tan(math.radians(a1))
print(' O numero é:{:.1f}\n E seu o seno é {:.2f}\n seu cosseno é {:.2f}\n E sua tangente é {:.2f}'.format(a1, s, c, t))