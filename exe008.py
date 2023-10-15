# Escreva um pragrama que leia um valor em metros e a exiba convertido em centímetros e milimetros.
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de \033[1m{}\033[mm corresponde a \033[1m{}\033[mcm e \033[1m{}\033[mmm'.format(medida, cm, mm))
