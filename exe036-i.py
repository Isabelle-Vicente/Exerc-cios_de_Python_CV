valorCasa = float(input('Quando custa a casa: '))
salário = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos pretende pagar a casa: '))
prestação = valorCasa / (anos * 12)
if prestação > (salário * 30 / 100):
    print('Empréstimo negado')
else:
    print('Empréstimo aprovando')
print('Valor da prestação é {}'.format(prestação))