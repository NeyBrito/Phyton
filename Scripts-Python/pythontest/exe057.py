# coding=utf-8
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
idade = int(input('Informe sua idade: '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:[M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


