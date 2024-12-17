produtos = []
carrinho = []

def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    marca_produto = input("Digite a marca do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    quantidade_produto = int(input("Insira a quantidade do produto ne estoque :"))

    produto = {
        "produto": nome_produto,
        "marca": marca_produto,
        "preco": preco_produto,
        "qunatidade": quantidade_produto

    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def produtos_estoque():
    for produto in produtos:
        for key, value in produto.items():
            print(f'{key}: {value}')


def adicionar_no_carrinho():
    selecionar_produto = input("Digite o nome do produto desejado: ")
    for produto in produtos:
        if produto['produto'].lower() == selecionar_produto.lower():
            carrinho.append(produto)
            print("Produto adicionado ao carrinho...")
        else:
            print("Produto não encontrado!")

def listar_produtos_carrinho():
    for produto in carrinho:
        for key, value in produto.items():
            print(f'{key}:{value}')

def remover_produto_carrinho():
    selecionar_produto = input("Digite o nome do produto desejado: ")
    for produto in produtos:
        if produto['produto'].lower() == selecionar_produto.lower():
            carrinho.remove(produto)
            print("Produto removido do carrinho...")
        else:
            print("Produto não encontrado!")

def finalizer_compra():

    resposta = input("Deseja finalizar a compra?(SIM/NAO): ")
    if resposta.lower() == 'sim':
        forma_pagamento = input("Qual a forma de pagamento? (Dinheiro, Cartão ou PIX): ")
        if forma_pagamento.lower() == 'dinheiro':
            print("Pagamento efetuado em dinheiro, obrigado pela preferencia!")
        elif forma_pagamento.lower() == 'cartao':
            print("Pagamento efetuado em dinheiro, obrigado pela preferencia!")
        elif forma_pagamento.lower() == 'pix':
            print("Pagamento efetuado com PIX, obrigado pela preferencia!")
        else:
            print("Indique uma forma de pagamento corresta!")
    




cadastrar_produto()
produtos_estoque()
adicionar_no_carrinho()
listar_produtos_carrinho()
remover_produto_carrinho()
finalizer_compra()



#if __name__ == "__main__":
#    menu()

'''
Cadastrar novos produtos

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