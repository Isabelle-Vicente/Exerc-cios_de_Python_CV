#Escreva um programa que converta uma temperatura digitada me °c e corverta °f.
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
