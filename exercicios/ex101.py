from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade >= 18 and idade < 65:
        return "VOTO OBRIGATÓRIO"
    elif idade > 65:
        return "VOTO OPCIONAL"
    else:
        return "NÃO VOTA"

print('-'*25)
anonasc = int(input('Em que ano voce nasceu? '))  
print(voto(anonasc))  