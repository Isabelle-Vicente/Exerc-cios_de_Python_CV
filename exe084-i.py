pessoas = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print("Ao todo, você cadastrou {} pessoas".format(len(pessoas)))
print(pessoas)