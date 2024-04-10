import json

atendimentos = []

def listar_atendimentos():
    print("Lista de atendimentos:")
    for atendimento in atendimentos:
        print(atendimento)

def criar_atendimento():
    atendimento = {}
    atendimento['id'] = len(atendimentos) + 1
    atendimento['descricao'] = input("Digite a descrição do atendimento: ")
    atendimento['data'] = input("Digite a data do atendimento: ")
    atendimentos.append(atendimento)
    print("Atendimento criado com sucesso!")

def atualizar_atendimento():
    id = int(input("Digite o ID do atendimento que deseja atualizar: "))
    for atendimento in atendimentos:
        if atendimento['id'] == id:
            atendimento['descricao'] = input("Digite a nova descrição do atendimento: ")
            atendimento['data'] = input("Digite a nova data do atendimento: ")
            print("Atendimento atualizado com sucesso!")
            return
    print("Atendimento não encontrado!")

def deletar_atendimento():
    id = int(input("Digite o ID do atendimento que deseja deletar: "))
    for atendimento in atendimentos:
        if atendimento['id'] == id:
            atendimentos.remove(atendimento)
            print("Atendimento deletado com sucesso!")
            return
    print("Atendimento não encontrado!")

def salvar_atendimentos():
    with open('atendimentos.json', 'w') as file:
        json.dump(atendimentos, file)

def carregar_atendimentos():
    global atendimentos
    try:
        with open('atendimentos.json', 'r') as file:
            atendimentos = json.load(file)
    except FileNotFoundError:
        pass

def main():
    carregar_atendimentos()
    while True:
        print("\n1. Listar atendimentos")
        print("2. Criar atendimento")
        print("3. Atualizar atendimento")
        print("4. Deletar atendimento")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_atendimentos()
        elif opcao == '2':
            criar_atendimento()
        elif opcao == '3':
            atualizar_atendimento()
        elif opcao == '4':
            deletar_atendimento()
        elif opcao == '5':
            salvar_atendimentos()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
