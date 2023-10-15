#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um numero: '))
print('Analisando o valor {}, seu antecessor é \033[34m{}\033[m e o sucessor é \033[31m{}\033[m'.format(n, (n-1), (n+1)))