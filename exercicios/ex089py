tabela = []

cont = -1
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    tabela.append([[nome, [n1,n2]], media])
    cond = ' '
    while cond not in 'SN':
        cond = input("Quer continuar [S/N] ").upper().strip()[:1]
    if cond == 'N':
        break
print('=-='*10)
print("No. NOME        MÉDIA")
print('-'*20)
for tab in tabela:
    cont+=1
    print(f"{cont:<4}{tab[0][0]:<13}", end='')
    print(f"{tab[1]:.1f}")
print('-'*34)
while True:
    n = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
    if n == 999:
        break
    else:
        print(f'As notas de {tabela[n][0][0]} são {tabela[n][0][1]}')
        print('-'*34)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')