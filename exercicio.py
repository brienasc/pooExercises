# Função para ler uma pessoa
def ler_pessoa():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    gestante = input("Gestante (s/n): ").strip().lower() == "s"
    pcd = input("PCD (s/n): ").strip().lower() == "s"

    # Verifica prioridade
    prioritario = idade >= 60 or gestante or pcd

    pessoa = {
        "nome": nome,
        "idade": idade,
        "gestante": gestante,
        "pcd": pcd,
        "prioritario": prioritario
    }

    print("PRIORITÁRIO" if prioritario else "NORMAL")
    return pessoa

# Programa principal
pessoas = []
N = int(input("Quantas pessoas deseja cadastrar? "))

for _ in range(N):
    pessoa = ler_pessoa()
    pessoas.append(pessoa)

# Contar prioritários e não prioritários
qtd_prioritarios = sum(1 for p in pessoas if p["prioritario"])
qtd_normais = N - qtd_prioritarios

print(f"\nTotal prioritários: {qtd_prioritarios}")
print(f"Total normais: {qtd_normais}")

# Remover a primeira pessoa não prioritária, se existir
for i, p in enumerate(pessoas):
    if not p["prioritario"]:
        print(f"\nRemovendo a primeira pessoa não prioritária: {p['nome']}")
        pessoas.pop(i)
        break

# Mostrar lista final
print("\nLista final de pessoas:")
for p in pessoas:
    print(p)