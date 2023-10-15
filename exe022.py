#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
frase = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é', frase.upper())
print('Seu nome em minúsculas é', frase.lower())
print('Seu nome tem ao todo letras', len(frase)-frase.count(' '))
print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))
