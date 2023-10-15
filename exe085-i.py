num = []
for c in range(10):
    num.append((int(input(f'Digite o numero {c}: '))))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break