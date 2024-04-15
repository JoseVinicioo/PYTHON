import emoji
print('/'*21)
print('\033[1;32mDADOS DO BRASILEIRÃO\033[m')
print('/'*21)
times = ('','Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Red Bull Bragantino','Fluminense','Athletico','Internacional','Fortaleza'
,'São Paulo'
,'Cuiabá'
,'Corinthians'
,'Cruzeiro'
,'Vasco'
,'Bahia'
,'Santos'
,'Goiás'
,'Coritiba'
,'América-MG')
print(emoji.emojize('TOP 5 :troféu:', language='pt'))
for cont in range(1, len(times[:6])):
    print(f'{cont}° {times[cont]}')
print(emoji.emojize('ULTIMOS 4 :gráfico_caindo:', language='pt'))
for cont2 in range(len(times[:20]), 16, -1):
    print(f'{cont2}° {times[cont2]}')
print(emoji.emojize('ORDEM ALFABETICA :letras_latinas:', language='pt'))
ordemm = sorted(times)
for ordem in ordemm[1:21]:
    print(ordem)
print(f'O time Cortiba esta na posição: {times.index('Coritiba')}')

