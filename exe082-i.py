numbers = []
impares = []
pares = []
while True:
    n = int(input('Digite um numero: '))
    numbers.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print(f"A lista completa é {numbers}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")