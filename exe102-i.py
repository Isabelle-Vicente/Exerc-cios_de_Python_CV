def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        f += c
        if show == True:
            print(f'{f} x ', end='')
    print(f"\nO fatorial de {num} é igual {f} ")


#Programa pricipal
fatorial(8, show=True)
