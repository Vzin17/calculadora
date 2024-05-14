numero = int(input("Digite um numero: "))
opcao = input("Digite se queres par ou impar ( P - I)")

for numero in range(1, numero + 1):
    if numero % 2 == 0:
        if opcao.upper() == "P":
            print(f"{numero} eh par!")
    else:
        if opcao.upper() == "I":
            print(f"{numero} eh impar!")

    