#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângula, calcule e mostre o comprimento hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('\033[31mA hipotenusa vai medir {:.2f}\033[m'.format(hi))