from datetime import date
print('Qual seu sexo?? ')
s = str(input('(1) - Masculino\n(2) - Feminino\n'))
n = int(input('Em que ano você nasceu? '))
idade = date.today().year - n
if s == '2':
    print('O alistamento não é obrigatorio para mulheres.')
elif s =='1' and idade < 18:
    print('Você naceu em {} tem {} anos em {}'.format(n,idade,date.today().year))
    print('Ainda falta {} anos para seu alistamento\nSeu alistamento sera em {}'.format(18-idade,n+18))
elif s == '1' and idade == 18:
    print('Você naceu em {} tem {} anos em {}'.format(n, idade, date.today().year))
    print('Tem que se alistar IMEDIATAMENTE!!')
elif s =='1' and idade > 18:
    print('Você naceu em {} tem {} anos em {}'.format(n,idade,date.today().year))
    print('Você ja devia ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(n + 18))

