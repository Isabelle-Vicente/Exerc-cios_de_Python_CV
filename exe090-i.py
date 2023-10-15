aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('A media de {} é: '.format(aluno['nome'])))
if aluno['media'] < 5:
    aluno['situação'] = 'REPROVADO'
elif aluno['media']  >= 5 and aluno['media'] <= 6.9:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVANDO'
print('-=' * 40)
print('O nome é igual {}'.format(aluno['nome']))
print('A media é igual a {}'.format(aluno['media']))
print('A situação do aluno é igual {}'.format(aluno['situação']))
print('-=' * 40)


