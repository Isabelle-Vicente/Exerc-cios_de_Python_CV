from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogodor= int(input('Qual é seu palpite? '))
    palpites += 1
    if jogodor == computador:
        acertou = True
    else:
        if jogodor < computador:
            print('Mais... Tente mais uma vez.')
        elif jogodor > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))