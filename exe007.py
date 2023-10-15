# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

m1 = float(input('Primeira nota do aluno: '))
m2 = float(input('Segunda nota do aluno: '))
m3 = float(input('Terceira nota do aluno: '))
m4 = float(input('Quarta nota do aluno: '))
mt = (m1 + m2 + m3 + m4)/4
print('\033[4mA media do aluno é {:.1f}\033[m'.format(mt))
