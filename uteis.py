def preços():
    valor = float(input('Digite o preço: R$'))
    metade = valor / 2
    dobro = valor * 2
    aumento = valor + (valor / 100) * 10
    print(f'A metade de {valor} é {metade}')
    print(f'O dobro de {valor} é {dobro}')
    print(f'Aumentado 10%, temos {aumento:.2f}')