# Inicializar a lista de tarefas
tarefas = []


def exibir_menu():
    print("""
        ----- MENU -----
        [1] Adicionar tarefa
        [2] Exibir tarefas
        [3] Marcar tarefa como concluída
        [4] Remover tarefa
        [0] Sair
        """)


def exibir_tarefas():
    if not tarefas:
        print("Nenheuma tarefa no momento.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluida" if tarefa["concluida"] else "Pendente"
            print(f'{i + 1}. {tarefa['descricao']} - {status}')


while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        descricao = input("Digite a descrição da tarefa: ")
        tarefa = {"descricao": descricao, "concluida": False}
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == 2:
        exibir_tarefas()

    elif opcao == 3:
        exibir_tarefas()
        numero = int(input("Digite o número da tarefa a ser marcada como concluída: "))
        if 0 < numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")

    elif opcao == 4:
        exibir_tarefas()
        numero = int(input("Digite o número da tarefa a ser removida: "))
        if 0 < numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido")

    elif opcao == 0:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. tente novamente.")