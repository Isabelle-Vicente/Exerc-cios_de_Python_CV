numbers = []
while True:
    num = int(input("Digite um valor: "))
    numbers.append(num)
    if num == 5:
        c = True
    else:
        c = False
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print("Você digitou {} elementos".format(len(numbers)))
print("Os valores em ordem decrescente são ", end='')
print(sorted(numbers, reverse=True))
if c == True:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")