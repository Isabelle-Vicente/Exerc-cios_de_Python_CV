from random import randint
from time import sleep
inf = {}
print("Valores sorteados: ")
for j in range(1, 5):
    num = randint(1, 6)
    inf['Jogador'] = (f"Jogador{j}")
    inf['num'] = (f'{num}')
    print(f"Jogador{j} tirou {num} no dado")
print('-=' * 40)
print(inf)