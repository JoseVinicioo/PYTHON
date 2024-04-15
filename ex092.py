from datetime import datetime

dados = dict()

dados['Nome'] = str(input('Nome: '))
anonasc = int(input('Data de nascimento: ')) 
dados['Idade'] = 2024 - anonasc
dados["Ctps"] = int(input('Carteira de Trabalho [diferente de 0]: '))
if dados['Ctps'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Sálario: R$'))
    dados['Aposentadoria'] = (dados['Ano de contratação'] + 35) - anonasc
for k,v in dados.items():
        print(f'{k} é igual a {v}')
