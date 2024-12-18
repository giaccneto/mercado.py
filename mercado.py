produtos = []
carrinho = []


def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    quantidade_produto = int(input("Insira a quantidade do produto ne estoque :"))

    produto = {
        "produto": nome_produto,
        "preco": preco_produto,
        "quantidade": quantidade_produto
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def produtos_estoque():
    for produto in produtos:
        for key, value in produto.items():
            print(f'{key}: {value}\n')


def adicionar_no_carrinho():
    selecionar_produto = input("Digite o nome do produto desejado: ")
    qtd = int(input("Digite a quantidade desejada: "))

    for produto in produtos:
        if qtd > produto["quantidade"]:
            print("Quantidade desejada indisponivel!")
        elif qtd <= 0:
            print('Quantidade deve ser um numero positivo!')
        elif produto["produto"].lower() == selecionar_produto.lower():
            carrinho.append({"produto": produto["produto"], "quantidade": qtd, "preco": produto["preco"]})
            print("Produto adicionado ao carrinho...")
        else:
            print("Produto não encontrado!")

# def listar_produtos_carrinho():
#     for produto in carrinho:
#         for key, value in produto.items():
#             print(f'{key}:{value}')


def remover_produto_carrinho():
    selecionar_produto = input("Digite o nome do produto desejado: ")
    for produto in carrinho:
        if produto['produto'].lower() == selecionar_produto.lower():
            carrinho.remove(produto)
            print("Produto removido do carrinho...")
        else:
            print("Produto não encontrado!")


def finalizer_compra():
    resposta = input("Deseja finalizar a compra?(SIM/NAO): ")
    if resposta.lower() == 'sim':
        calcular_carinho()
        forma_pagamento = input("Qual a forma de pagamento? (Dinheiro, Cartão ou PIX): ")

        if forma_pagamento.lower() == 'dinheiro':
            print("Pagamento efetuado em dinheiro, obrigado pela preferencia!")
        elif forma_pagamento.lower() == 'cartao':
            print("Pagamento efetuado em dinheiro, obrigado pela preferencia!")
        elif forma_pagamento.lower() == 'pix':
            print("Pagamento efetuado com PIX, obrigado pela preferencia!")
        else:
            print("Indique uma forma de pagamento corresta!")
    atualizar_estoque()


def atualizar_estoque():
    for prod in produtos:
        for item in carrinho:
            if item['produto'] == prod['produto']:
                prod['quantidade'] -= item['quantidade']



def calcular_carinho():
    valor = 0.0
    for prod in carrinho:
        prod['preco'] *= prod['quantidade']
        valor += prod['preco']
    print(f'Total a pagar R$ {valor}')

def ver_carrinho():
    for produto in carrinho:
        for key, value in produto.items():
            print(f'{key}: {value}')


def menu():
    while True:
        opcao = input("Escolha uma opção: "
                      "\n1 - CADASTRAR PRODUTO: "
                      "\n2 - VER PRODUTOS DISPONIVEIS: "
                      "\n3 - ADICIONAR UM PRODUTO NO CARINHO: "
                      "\n4 - REMOVER UM PRODUTO DO CARRINHO: "
                      "\n5 - VER CARRINHO DE COMPRAS: "
                      "\n6 - FINALIZAR A COMPRA: "
                      "\n0 - PARA SAIR: ")
        if opcao == "0":
            print("Saindo do sistema...")
            break
        elif opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            produtos_estoque()
        elif opcao == "3":
            adicionar_no_carrinho()
        elif opcao == "4":
            remover_produto_carrinho()
        elif opcao == "5":
            ver_carrinho()
        elif opcao == "6":
            finalizer_compra()
        else:
            print("Entrar uma opção valida!")


if __name__ == "__main__":
    menu()

'''
Cadastrar novos produtos    ok

○ Listar os produtos em estoque     OK

○ Adicionar produtos ao carrinho    OK

○ Remover produtos do carrinho     OK 

○ Finalizar a compra (atualizando o estoque)

○ Sempre que uma ação for realizada (cadastrar produto, adicionar ao carrinho), a interface deve ser atualizada para refletir as
mudanças.

○ Verificar se os dados inseridos pelo usuário são válidos (por exemplo, se o preço é um número positivo).

○ Ao finalizar a compra, atualizar a quantidade em estoque dos produtos.

○ Implementar funcionalidades adicionais como busca de produtos, descontos, etc.
'''
