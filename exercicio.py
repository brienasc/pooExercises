from collections import deque

# Filas
fila_prioritaria = deque()
fila_normal = deque()

# Estatísticas
atendidos_total = 0
atendidos_prioritarios = 0
atendidos_normais = 0


def eh_prioritario(idade: int, gestante: bool, pcd: bool) -> bool:
    """Regra de prioridade: idade >= 60 ou gestante ou pcd"""
    return idade >= 60 or gestante or pcd


def adicionar_cliente():
    nome = input("Nome: ").strip()
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida, tente novamente.")
        return

    gestante = input("Gestante (s/n): ").strip().lower() == "s"
    pcd = input("PCD (s/n): ").strip().lower() == "s"

    cliente = {"nome": nome, "idade": idade, "gestante": gestante, "pcd": pcd}

    if eh_prioritario(idade, gestante, pcd):
        fila_prioritaria.append(cliente)
        print(f"{nome} adicionado à fila PRIORITÁRIA.")
    else:
        fila_normal.append(cliente)
        print(f"{nome} adicionado à fila NORMAL.")


def atender_proximo():
    global atendidos_total, atendidos_prioritarios, atendidos_normais

    if fila_prioritaria:
        cliente = fila_prioritaria.popleft()
        print(f"Atendendo prioritário: {cliente['nome']}")
        atendidos_prioritarios += 1
    elif fila_normal:
        cliente = fila_normal.popleft()
        print(f"Atendendo normal: {cliente['nome']}")
        atendidos_normais += 1
    else:
        print("Nenhum cliente na fila.")
        return

    atendidos_total += 1


def listar_filas():
    print("\nFila PRIORITÁRIA:")
    for c in fila_prioritaria:
        print(f"- {c['nome']} (idade {c['idade']}, gestante={c['gestante']}, pcd={c['pcd']})")

    print("\nFila NORMAL:")
    for c in fila_normal:
        print(f"- {c['nome']} (idade {c['idade']})")

    if not fila_prioritaria and not fila_normal:
        print("Nenhum cliente nas filas.")


def relatorio():
    print("\n--- RELATÓRIO ---")
    print(f"Total atendidos: {atendidos_total}")
    print(f"Atendidos prioritários: {atendidos_prioritarios}")
    print(f"Atendidos normais: {atendidos_normais}")
    print(f"Clientes na fila prioritária: {len(fila_prioritaria)}")
    print(f"Clientes na fila normal: {len(fila_normal)}")

    if atendidos_total > 0:
        perc_prioritarios = (atendidos_prioritarios / atendidos_total) * 100
        print(f"Percentual de prioritários atendidos: {perc_prioritarios:.2f}%")
    else:
        print("Ainda não houve atendimentos.")


# Loop do menu
while True:
    print("\n--- MENU ---")
    print("1. Adicionar cliente")
    print("2. Atender próximo")
    print("3. Listar filas")
    print("4. Relatório")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        atender_proximo()
    elif opcao == "3":
        listar_filas()
    elif opcao == "4":
        relatorio()
    elif opcao == "5":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")