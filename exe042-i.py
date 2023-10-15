print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segndo segmeto: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAM triâgulo!')
    if r1 == r2 == r3:
        print('O triagulo é Equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triagulo é Isósceles')
    elif r1 != r2 != r3:
        print('O triagulo é Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo!')