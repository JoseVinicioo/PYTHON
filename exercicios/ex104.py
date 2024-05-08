def leiaInt(prompt):
    ok = False
    valor = 0
    while True:
        n = str(input(prompt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO!! Digite um valor inteiro valido.\033[m')
        if ok:
            break
    return valor

    """ while True:
        entrada = input(prompt)
        if entrada.isdigit():
            break
        else:
            print('\033[1;31mERRO!! Digidte um valor inteiro valido.\033[m') """

n = leiaInt("Digite algum número: ")
print(f'Voce digitou o valor {n}')