import os
while True:
    os.system("cls")
    print("Tabuada simples")
    tabuada = []
    try:
        x = float(input("Digite aqui um número: "))
    except ValueError:
       print("Erro, digite um número")
       continue
    for i in range(11):
        result = x * i
        tabuada.append(result)
        print(f"{x} * {i} = {result}")
    tabX = x * x
    tabuada.append(tabX)
    print(f"A tubuada do número {x} é: {tabuada}")
    fim = str(input("Deseja continuar? (S/N)")).lower()
    if fim != "s":
        break