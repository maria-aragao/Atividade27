# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

def gerenciar_convidados():
    convidados = []
    total_convidados = 7

    for i in range(total_convidados):
        nome = input(f"Digite o nome do convidado {i + 1}: ")
        convidados.append(nome)

    remover = input("Deseja remover algum convidado da lista? (sim/não): ").strip().lower()
    
    if remover == 'sim':
        nome_remover = input("Digite o nome do convidado a ser removido: ")
        
        if nome_remover in convidados:
            convidados.remove(nome_remover)
            print(f"{nome_remover} foi removido da lista.")
        else:
            print(f"{nome_remover} não está na lista de convidados.")

    print("\nLista final de convidados:")
    for convidado in convidados:
        print(convidado)

gerenciar_convidados()
