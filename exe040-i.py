nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('O Aluno foi REPROVADO')
elif media > 5.0 and media < 6.9:
    print('O Aluno esta de RECUPERAÇãO')
else:
    print('O Aluno foi APROVADO')