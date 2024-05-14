print("Bem-vindo à calculadora! Digite os números seguidos de 'Enter'. Digite 'P' para parar e 'X' para sair.")

while True:
    operacao = input("Digite a operação desejada (+, -, *, /): ").strip().lower()
    
    if operacao == 'x':
        print("Encerrando a calculadora. Adeus!")
        break

    if operacao not in ('+', '-', '*', '/'):
        print("Operação inválida. Tente novamente.")
        continue

    numeros = []
    while True:
        entrada = input("Digite um número ou 'P' para parar: ").strip().lower()
        if entrada == 'p':
            break
        
        numero = float(entrada)
        numeros.append(numero)
    
    if not numeros:
        print("Nenhum número fornecido. Operação cancelada.")
        continue
    
    if operacao == '+':
        resultado = sum(numeros)
    elif operacao == '-':
        resultado = numeros[0] - sum(numeros[1:])
    elif operacao == '*':
        resultado = 1
        for num in numeros:
            resultado *= num
    elif operacao == '/':
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                print("Erro: Divisão por zero!")
                break
            resultado /= num
    
    print("Resultado:", resultado)
