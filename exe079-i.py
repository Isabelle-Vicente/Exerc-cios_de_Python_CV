numbers = []

while True:
    num = int(input("Digite um valor: "))
    if num not in numbers:
        numbers.append(num)
    else:
        print("Valor duplicado! Não vou adicionar")
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(numbers)