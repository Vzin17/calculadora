'''
for num in range(500):
    print(f"N: {num}")
    if num == 50:
        break


for num in range(10):
    if num % 3 == 0:
        continue
    
    print(f"N: {num}")
'''

while True:
    opcao = input("Digite X para sair: ")
    print(opcao)
    if opcao.upper() == 'X':
        break
