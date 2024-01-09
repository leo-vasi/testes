import os
os.system("cls")
print("Lista que recebe um número X de números e depois mostra o maior valor dentre esses números")
num = []
x = int(input("Digite quantos números irão na lista: "))
for i in range(x):
    num.append(int(input(f"Digite aqui o {i+1}º número: ")))
maior = max(num)
print(f"O maior valor é: {maior}") 