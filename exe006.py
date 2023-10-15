# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero: '))
print('\033[30;41mO dobro de {} vale {}\033[m'.format(n, n*2))
print('\033[30;42mO triplo de {} vale {}\033[m'.format(n, n*3))
print('\033[30;43mA raiz quadrada de {} é igual a {}\033[m'.format(n, pow(n, (1/2))))

