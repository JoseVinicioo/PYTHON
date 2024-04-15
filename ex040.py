n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
media = (n1 + n2) /2
if media < 5:
    print('\033[1;31mVOCÊ FOI REPROVADO COM A MEDIA:\033[1;97;41m{:.1f}\033[m'.format(media))
elif 5 <= media <= 6.9:
    print('\033[1;34mVOCÊ ESTÁ DE RECUPERAÇÃO COM A MEDIA:\033[1;97;44m{:.1f}\033[m'.format(media))
elif media >= 7.0:
    print('\033[1;32mVOCÊ FOI APROVADO COM MEDIA:\033[1;97;42m{:.f}\033[m'.format(media))