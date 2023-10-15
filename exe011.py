#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de \033[7m{}m2\033[m'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de \033[7m{}l\033[m de tinta.'.format(tinta))
