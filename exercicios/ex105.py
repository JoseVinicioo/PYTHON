def notas(*notas, sit=False):
    """
    notas(*notas, sit=False)
    -> Função para analisar notas e a situação de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['média'] = sum(notas)/len(notas)
    if sit:
        if dados['média'] >= 7:
            dados['situacao'] = "Boa"
        elif dados['média'] <= 5.9:
            dados['situacao'] = "Ruim"
        else:
            dados['situacao'] = "Razoável"
    return dados

resp = notas(3.5,2,6.5,2,7,4)
print(resp)