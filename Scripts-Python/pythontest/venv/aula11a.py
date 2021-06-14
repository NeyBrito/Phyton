#a = 3
#b = 5
#print('Os valores são \033[7;30m {} \033[m e \033[7;30m {}\033[m'.format(a, b))
nome = 'Ney Brito'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'negrito' : '\033[1m'}
#print('Olá muito prazer em te conhecer, {} {} {}!'.format('', nome , ''))
print('Olá muito prazer em te conhecer, {} {} {}!'.format( cores['pretoebranco'], nome , cores['limpa']))