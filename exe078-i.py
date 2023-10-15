numbers = list()
maior = 0
menor = 0
quant = 0
for p in range(5):
    num = int(input(f"Digite um numero na posição {p}: "))
    numbers.append(num)
    quant += 1
    if quant == 1:
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(numbers)
print(f"O maior numero é {maior} ele está na posição ", end='')
for c, v in enumerate(numbers):
    if v == maior:
        print(f'{c}...', end='')
print(f"\nO menor numero é {menor} ele está na posição ", end='')
for c, v in enumerate(numbers):
    if v == menor:
        print(f'{c}...', end='')