def Omaior():
    numbers = list()
    resp = ""
    while resp in "Ss":
        num = int(input("Digite um numero: "))
        numbers.append(num)
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont = (len(numbers))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print("Analisando os valores passados...", end='')
    print(numbers)
    print(f"Foram informados {cont} valores ao todo.")
    print("O maior valor informado foi ", max(numbers))

#Programa Principal
Omaior()