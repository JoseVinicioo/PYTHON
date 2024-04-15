from time import sleep
print('-_-' *10)
print('  \033[1;97;41mEMPRESTIMO BANCO DO SEU ZÉ\033[m')
print('-_-' *10)
sleep(1.2)
c = float(input('\033[1;31mQual o valor da casa? R$\033[m'))
sleep(0.5)
s = float(input('\033[1;97mQual seu salário? R$\033[m'))
sleep(0.5)
a = int(input('\033[1;31mEm quantos anos deseja pagar? R$\033[m'))
sleep(0.5)
m = c/(a*12)
if m >= s * 30/100:
    print('\033[7;31mSeu emprestimo foi negado!\033[m')
else:
    print('\033[1;32mSeu emprestimo foi aprovado!!\nVocê irá pagar {:.2f}R$ mensalmente\033[m'.format(m))
print('Agradecemos o acesso!')