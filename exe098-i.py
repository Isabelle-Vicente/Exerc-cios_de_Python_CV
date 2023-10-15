def contador():
    print("Contagem de 1 até 10 em 1")
    for n in range(1, 11):
        print(n, end=' ')
    print('FIM')
    print("Contagem de 10 até 2 em 2")
    for n in range(10, -1, -2):
        print(n, end=' ')
    print('FIM')
    inicio = int(input("INICIO: "))
    fim = int(input("FIM: "))
    passo = int(input("PASSO:"))
    for n in range(inicio, fim, passo):
        print(n, end=' ')

#Programa Principal
contador()