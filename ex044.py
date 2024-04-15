p = float(input('Preço das comprar: R$ '))
c = str(input("FORMAS DE PAGAMENTO: \n(1) - À vista dinheiro/cheque\n(2) - "
              "À vista no cartão \n(3) - Ate 2x no cartão \n(4) - "
              "3x ou mais no cartão\nEscolha uma opção: "))
if c == '1':
    c = p - (10/100*p)
elif c == '2':
    c = p - (5 / 100 * p)
elif c == '3':
    c = p
    print('Sua comprar sera parcelada em 2x de R${:.2f} SEM JUROS'.format(p / 2))
elif c == '4':
    par = int(input('Quantas parcelas? '))
    c =p + (20/100 * p)
    print('Sua comprar sera parcelada em {}x de R${:.2f} COM JUROS'.format(par,c/par))
else:
    c = p
    print('\033[1;31mOPÇÃO INVALIDA!! Tente novamente!')
print('Sua compra de {}R$, vai custar {}R$ no final'.format(p,c))