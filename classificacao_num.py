import os
os.system("cls")
print("\n\tPrograma que classifica números em categorias como positivo, negativo ou zero")
positivos = []
negativos = []
zeros = []
while True:
    for i in range(5):
        num = float(input("Digite aqui um número: "))
        nova_tentativa = str(input("Deseja adicionar novo número? (S/N) ")).lower()
        if nova_tentativa == 'n':
            print("Lista encerrada")
            break
        else:
            if num == 0:
                zeros.append(num)
            elif num < 0:
                negativos.append(num)
            elif num > 0:
                positivos.append(num)
    print("Números positivos: ", positivos, "Números negativos: ", negativos, "Zeros: ", zeros)