produtos = []
carrinho = []


def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ").strip()
    try:
        preco_produto = float(input("Digite o preço do produto: "))
        quantidade_produto = int(input("Insira a quantidade do produto no estoque: "))
        if preco_produto < 0 or quantidade_produto < 0:
            print("Preço e quantidade devem ser valores positivos.")
            return
    except ValueError:
        print("Preço e quantidade devem ser valores numéricos.")
        return

    produto = {
        "produto": nome_produto,
        "preco": preco_produto,
        "quantidade": quantidade_produto
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def produtos_estoque():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print("\n".join([f"{key}: {value}" for key, value in produto.items()]))
        print("-—-")


def adicionar_no_carrinho():
    selecionar_produto = input("Digite o nome do produto desejado: ").strip()
    try:
        qtd = int(input("Digite a quantidade desejada: "))
        if qtd <= 0:
            print("Quantidade deve ser um número positivo!")
            return
    except ValueError:
        print("Quantidade deve ser um número inteiro.")
        return

    for produto in produtos:
        if produto["produto"].lower() == selecionar_produto.lower():
            if qtd > produto["quantidade"]:
                print("Quantidade desejada indisponível!")
                return
            carrinho.append({"produto": produto["produto"], "quantidade": qtd, "preco": produto["preco"]})
            atualizar_estoque()
            print("Produto adicionado ao carrinho.")
            return

    print("Produto não encontrado!")



def remover_produto_carrinho():
    selecionar_produto = input("Digite o nome do produto a ser removido: ").strip()
    qtd = int(input("Insira a quantidade do produto a ser removida: "))

    for item in carrinho:
        if item['produto'].lower() == selecionar_produto.lower():
            if qtd > item['quantidade']:
                print(f"A quantidade removida ({qtd}) é maior que a quantidade no carrinho ({item['quantidade']}).")
                return

            atualizar_retirando_carrinho(item['produto'], qtd)

            item['quantidade'] -= qtd
            if item['quantidade'] == 0:
                carrinho.remove(item)

            print("Produto removido do carrinho.")
            return

    print("Produto não encontrado no carrinho!")


def finalizar_compra():
    resposta = input("Deseja finalizar a compra? (SIM/NAO): ").strip().lower()
    if resposta == 'sim':
        calcular_total_carrinho()
        forma_pagamento = input("Qual a forma de pagamento? (Dinheiro, Cartão ou PIX): ").strip().lower()
        if forma_pagamento in ['dinheiro', 'cartão', 'pix']:
            print(f"Pagamento efetuado com {forma_pagamento}, obrigado pela preferência!")
        else:
            print("Forma de pagamento inválida.")
        #atualizar_estoque()
        carrinho.clear()
    else:
        print("Compra não finalizada.")


def atualizar_estoque():
    for prod in produtos:
        for item in carrinho:
            if item['produto'] == prod['produto']:
                prod['quantidade'] -= item['quantidade']


def atualizar_retirando_carrinho(produto_nome, qtd):
    for prod in produtos:
        if prod['produto'].lower() == produto_nome.lower():
            prod['quantidade'] += qtd
            return

def calcular_total_carrinho():
    total = sum(prod['preco'] * prod['quantidade'] for prod in carrinho)
    print(f"Total a pagar: R$ {total:.2f}")


def ver_carrinho():
    if not carrinho:
        print("Carrinho está vazio.")
        return
    for produto in carrinho:
        print("\n".join([f"{key}: {value}" for key, value in produto.items()]))
        print("-—-")
    calcular_total_carrinho()


def menu():
    opcoes = {
        "1": cadastrar_produto,
        "2": produtos_estoque,
        "3": adicionar_no_carrinho,
        "4": remover_produto_carrinho,
        "5": ver_carrinho,
        "6": finalizar_compra
    }
    while True:
        opcao = input("""
Escolha uma opção: 
1 - Cadastrar Produto
2 - Ver Produtos Disponíveis
3 - Adicionar Produto no Carrinho
4 - Remover Produto do Carrinho
5 - Ver Carrinho de Compras
6 - Finalizar a Compra
0 - Sair do Sistema
Opção: """).strip()
        if opcao == "0":
            print("Saindo do sistema...")
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
