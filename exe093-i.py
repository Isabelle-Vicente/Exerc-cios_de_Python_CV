jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}: '))
print('-=' * 40)
print(gols)