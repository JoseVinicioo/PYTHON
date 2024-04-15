n = str(input('Digite um nome: '))
s = str(input('O sexo [F/M]: ')).strip().upper()[0]
while s != 'F' and s != 'M':
        s = str(input('Resposta invalida, digite um valor valido [F/M]')).strip().upper()[0]
if s == 'M':
    s = 'Masculino'
if s == 'F':
    s = 'Feminino'
print('RESPOSTA VALIDA!!\nNome: {}\nSexo: {}'.format(n,s))
