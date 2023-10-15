from datetime import date

def vontação():
    atual = date.today().year
    nasc = int(input('Em que ano você nasceu: '))
    idade = atual - nasc
    if idade >= 16 and idade < 18 or idade >= 60:
        print(f"Com {idade} anos: O VOTO É OPCIONAL")
    elif idade < 16:
        print(f"Com {idade} anos: VOCÊ NÃO PODE VOTAR")
    else:
        print(f"Com {idade} anos: O VOTO É OBRIGATORIO")

#Programa Principal
vontação()