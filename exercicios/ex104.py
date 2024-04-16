def leiaInt(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit():
            break
        else:
            print('\033[1;31mERRO!! Digidte um valor inteiro valido.\033[m')

n = leiaInt("Digite algum número: ")
print(f'Voce digitou o valor {n}')