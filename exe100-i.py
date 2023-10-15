def sortearsoma():
    from random import randint
    numbers = []
    totalpar = 0
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(5):
        sortea = randint(0, 100)
        numbers.append(sortea)
        if sortea % 2 == 0:
            totalpar = totalpar + sortea
        print(sortea , end=' ')
    print("Pronto!")
    print(f"Somando os valores pares de {numbers}, termos {totalpar}")

#Programa Principal
sortearsoma()