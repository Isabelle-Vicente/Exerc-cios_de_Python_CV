from datetime import date
trabalhador = {}
atual = date.today().year
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = int(input('Ano de Nascimento: '))
trabalhador['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['carteira'] != 0:
    trabalhador['anoc'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salario: '))
    print('- nome tem o valor {}'.format(trabalhador['nome']))
    print('- idade tem o valor {}'.format(atual - trabalhador['idade']))
    print('- ctps tem o valor {}'.format(trabalhador['carteira']))
    print('- contratação tem o valor {}'.format(trabalhador['anoc']))
    print('- salário tem o valor {}'.format(trabalhador['salario']))
    tempotrabalho = atual - trabalhador['anoc']
    aponsetar = 65 - tempotrabalho
    trabalhador['aponseta'] = aponsetar + (atual - trabalhador['idade'])
    print('- aposentadoria tem o valor {}'.format(trabalhador['aponseta']))
else:
    print('- nome tem o valor {}'.format(trabalhador['nome']))
    print('- idade tem o valor {}'.format(atual - trabalhador['idade']))
    print('- ctps tem valor 0')
