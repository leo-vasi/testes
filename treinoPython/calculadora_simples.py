import os
os.system("cls")
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("0. Sair")
while True:
    op = str(input("Digite a operação desejada: "))
    if op == 0:
        print("Fim")
        break
    else:
        x = float(input("Digite um número: "))
        y = float(input("Digite outro número: "))
        if op == '1':
            resultado = x + y
        elif op == '2':
            resultado = x - y
        elif op == '3':
            resultado = x * y
        elif op == '4':
            if y == 0:
                print("Não é possível dividir por zero.")
                continue
            resultado = x / y
        else:
            print("Operação inválida.")
            continue
        print(resultado)
        nova_op = str(input("Deseja fazer outra operação? (S/N): ")).lower()
        if nova_op == "n":
            print("Fim")
            break
