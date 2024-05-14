while True:
    print("Calculadora estilo HP")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "X" or opcao == "x":
        print("Saindo...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Escolha novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
        print("Resultado da adição:", resultado)
    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)
    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)
    elif opcao == "4":
        if num2 == 0:
            print("Erro: Divisão por zero.")
        else:
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)

    continuar = input("Digite 'P' para continuar, ou qualquer outra tecla para voltar ao menu: ")
    if continuar != "P" and continuar != "p":
        continue
