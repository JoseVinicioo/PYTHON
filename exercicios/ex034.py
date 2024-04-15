s = float(input('Digite o valor do salario de um funcionario: '))
if s > 1250.00:
    n = (0.1 * s) + s
else:
    n = (0.15 * s) + s
print('Esse salario de {}R$, com o aumento de 15% passa a ser: {}R$'.format(s,n))