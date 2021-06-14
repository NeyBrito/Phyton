frase = str(input('Digite uma frase qualquer: '))
n1 = frase.upper().lower().count('a')
p1 = frase.upper().lower().find('a')
p2 = frase.upper().lower().rfind('a')
print('Essa frase tem {} letras a, sua primeira posição é {} e sua ultima posição é {}'.format(n1, p1, p2))

