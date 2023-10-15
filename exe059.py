# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
print('''[ 1 ] soma
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa''')
opção = 0
while opção != 5:
    opção = int(input('Digite a opção: '))
    if opção == 1:
        s = num1 + num2
        print('A soma dos numeros {} e {} é igual a {}'.format(num1, num2, s))
    elif opção == 2:
        m = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1,num2, m))
    elif opção == 3:
        if num1 > num2:
            print('O maior numero é {} e o menor é {}'.format(num1, num2))
        else:
            print('O maior numero é {} e o menor é {}'.format(num2, num1))
    elif opção == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    else:
        print('Opção invalida, Tente novamente')
print('ACABOU')

