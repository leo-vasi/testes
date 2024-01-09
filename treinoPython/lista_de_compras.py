import os
os.system("cls")
print("Lista de compras modificável ")
lista_de_compras = []
while True:
    qtd_produtos = int(input("Digite aqui quantos produtos você quer comprar (ou digite 0 (Zero) para encerrar a lista: )"))
    if qtd_produtos <= 0:
        print("Lista encerrada")
        break
    for i in range(qtd_produtos):
        produto = str(input(f"Digite aqui o {i+1}º item da sua lista de compras: "))
        lista_de_compras.append(produto)
    print("Lista de compras atual: ", lista_de_compras)
    fim = str(input("Deseja encerrar a lista? (S/N): ")).lower()
    if fim == "s":
        print("Lista de compras encerrada")
        break
    novo_item = str(input("Deseja adicionar novo item na lista? (S/N): ")).lower()
    if novo_item == "n":
        print("Lista encerrada")
        break
    novo_produto = str(input("Digite aqui o nome do novo produto: "))
    lista_de_compras.append(novo_produto)
    print("Lista final de compras: ", lista_de_compras)