def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        if x != 0:
            return x / y
    except ZeroDivisionError:
        return "Erro: Divisão por zero não permitida."


while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    try:
        escolha = int(input("Digite sua escolha (1/2/3/4/5): "))
    except ValueError:
        print("Por favor, digite um número válido para a operação.")
        continue

    if escolha == 5:
        print("Encerrando a calculadora...")
        break

    if escolha not in [1, 2, 3, 4]:
        print("Operação inválida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite números válidos.")
        continue

    if escolha == 1:
        print(f"Resultado: {add(num1, num2)}")
    elif escolha == 2:
        print(f"Resultado: {subtract(num1, num2)}")
    elif escolha == 3:
        print(f"Resultado: {multiply(num1, num2)}")
    elif escolha == 4:
        print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Opção inválida.")
