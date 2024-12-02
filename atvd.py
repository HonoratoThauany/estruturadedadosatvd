tarefas = []
estados = []

def adicionar_tarefa(nome):
    """Adiciona uma nova tarefa como pendente."""
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def marcar_concluida(indice):
    """Marca uma tarefa como concluída."""
    if 0 <= indice < len(tarefas):
        estados[indice] = "concluída"
        print(f"Tarefa '{tarefas[indice]}' marcada como concluída.")
    else:
        print("Índice inválido.")

def remover_tarefa(indice):
    """Remove uma tarefa da lista."""
    if 0 <= indice < len(tarefas):
        print(f"Tarefa '{tarefas[indice]}' removida.")
        tarefas.pop(indice)
        estados.pop(indice)
    else:
        print("Índice inválido.")

def listar_tarefas():
    """Lista todas as tarefas, separadas por estado."""
    print("\nTarefas Pendentes:")
    for i, (tarefa, estado) in enumerate(zip(tarefas, estados)):
        if estado == "pendente":
            print(f"{i}. {tarefa}")
    print("\nTarefas Concluídas:")
    for i, (tarefa, estado) in enumerate(zip(tarefas, estados)):
        if estado == "concluída":
            print(f"{i}. {tarefa}")

def pesquisar_tarefa(nome):
    """Pesquisa uma tarefa pelo nome."""
    for i, tarefa in enumerate(tarefas):
        if tarefa.lower() == nome.lower():
            print(f"Tarefa encontrada: {tarefa} (Estado: {estados[i]})")
            return
    print("Tarefa não encontrada.")

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Concluída")
    print("3. Remover Tarefa")
    print("4. Listar Tarefas")
    print("5. Pesquisar Tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)
    elif opcao == "2":
        listar_tarefas()
        indice = int(input("Digite o índice da tarefa a marcar como concluída: "))
        marcar_concluida(indice)
    elif opcao == "3":
        listar_tarefas()
        indice = int(input("Digite o índice da tarefa a remover: "))
        remover_tarefa(indice)
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        nome = input("Digite o nome da tarefa a pesquisar: ")
        pesquisar_tarefa(nome)
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
