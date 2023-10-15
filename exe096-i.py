def calcula_area():
    print("CONTROLE DE TERRENOS")
    print("----------------------")
    largura = float(input("Largura (m):"))
    comprimento = float(input("Comprimento (m)"))
    area = largura*comprimento
    print(f"A area de um terreno {largura}x{comprimento} é de {area}m2")

#Programa Principal
calcula_area()