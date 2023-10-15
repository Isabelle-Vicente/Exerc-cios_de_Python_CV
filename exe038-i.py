num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva outro numero: '))
if num1 > num2:
    print('O numero {} e maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} e maior que o numero {}'.format(num2, num1))
else:
    print('O numero {} e igual ao numero {}'.format(num1, num2))