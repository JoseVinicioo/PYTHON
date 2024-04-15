n = float(input('Qual é o salário do funcionario? R$'))
no = n + (n * 15/100)
print('O funcionario que ganhava {}, com 15% de aumento, passa a receber {:.2f}R$' .format(n,no))