pala = ('APRENDER','TESTAR','CURSO','PRATICAR','PYTHON','GUSTAVO','GUANABARA','CURSO EM VIDO')
for c in pala:
    print(f'\nNa palavra {c} temos: ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')
