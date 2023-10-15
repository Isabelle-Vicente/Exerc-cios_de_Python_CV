#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.21
print('Com \033[4mR${:.2f}\033[m você pode comprar \033[31mUS${:.2f}\033[m'.format(real, dolar))