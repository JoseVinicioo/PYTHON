aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
        aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')