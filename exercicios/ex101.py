def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

print('-'*25)
anonasc = int(input('Em que ano voce nasceu? '))  
print(voto(anonasc))  