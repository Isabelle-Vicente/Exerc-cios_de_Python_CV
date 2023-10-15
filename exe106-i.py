def ajuda():
    print('=' * 30)
    print('   SISTEMA DE AJUDA PyHELP')
    print('=' * 30)
    n = input("Função ou Biblioteca > ")
    help(n)


#Programa principal
ajuda()