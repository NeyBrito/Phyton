nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem normal no Brasil.')
elif nome in 'Ana Cládia Jéssica Juliana':
    print('Belo nome faminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))