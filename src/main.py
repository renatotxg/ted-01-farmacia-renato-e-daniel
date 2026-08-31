import csv

produtos = []

with open("dados/produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        produto = {
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": float(linha[3])
            
        }
        produtos.append(produto)


vendas = []

with open("dados/vendas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        venda = {
            "id": linha[0],
            "cliente": linha[1],
            "produto": linha[2],
            "quantidade": int(linha[3]),
            "valor_total": float(linha[4]),
            "canal": linha[5]
        }
        vendas.append(venda)


produtos_por_id = {}
for produto in produtos:
    produtos_por_id[produto["id"]] = produto


def faturamento_categoria(vendas, produtos_por_id):
    faturamento = {}

    for venda in vendas:
        produto = produtos_por_id[venda["produto"]]
        categoria = produto["categoria"]

        if categoria not in faturamento:
            faturamento[categoria] = 0

        faturamento[categoria] += venda["valor_total"]

    return faturamento

resultado = faturamento_categoria(vendas, produtos_por_id)

print("\n -- Faturamento Por Categoria -- ")

for categoria, valor in resultado.items():
    print(f"{categoria}: R$ {valor:.2f}")

def produtos_mais_vendidos(vendas, produtos_por_id):
    quantidade_produtos = {}

    for venda in vendas:
        id_produto = venda["produto"]
        quantidade = venda["quantidade"]

        if id_produto not in quantidade_produtos:
            quantidade_produtos[id_produto] = 0

        quantidade_produtos[id_produto] += quantidade

    return quantidade_produtos

resultado_produtos = produtos_mais_vendidos(vendas, produtos_por_id)

print("\n -- Produtos Mais Vendidos --")

for id_produto, quantidade in resultado_produtos.items():
    nome = produtos_por_id[id_produto]["nome"]
    print(f"{nome}: {quantidade} unidades")

def produto_mais_vendido(vendas, produtos_por_id):
    quantidade_por_produto = {}

    for venda in vendas:
        produto_id = venda["produto"]
        quantidade = venda["quantidade"]

        if produto_id in quantidade_por_produto:
            quantidade_por_produto[produto_id] += quantidade
        else:
            quantidade_por_produto[produto_id] = quantidade

    produto_id_mais_vendido = max(
        quantidade_por_produto,
        key=quantidade_por_produto.get
    )

    nome_produto = produtos_por_id[produto_id_mais_vendido]["nome"]
    quantidade_vendida = quantidade_por_produto[produto_id_mais_vendido]

    return nome_produto, quantidade_vendida

produto, quantidade = produto_mais_vendido(vendas, produtos_por_id)

print('\n -- Produto Mais Vendido --')
print(f"{produto}: {quantidade} unidades vendidas")


# conjunto de clientes unicos
clientes_unicos = set()

for venda in vendas:
    clientes_unicos.add(venda["cliente"])

print("\n -- Clientes Únicos -- ")
print(f"Quantidade de clientes diferentes: {len(clientes_unicos)}")
print(clientes_unicos)


#Operacao com conjuntos
clientes_balcao = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Balcão"

}

clientes_delivery_set = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Delivery"
}


clientes_ambos = clientes_balcao.intersection(clientes_delivery_set)

print("\n -- Clientes Que Compraram Nos Dois Canais -- ")
print(clientes_ambos)
#List Comprehension
produtos_caros = [
    produto["nome"]
    for produto in produtos
    if produto["preco"] > 30
]

print("\n -- Produtos acima de R$ 30 --")

for produto in produtos_caros:
    print(produto)

# Segunda List COmprehension
vendas_delivery = [
    venda
    for venda in vendas
    if venda["canal"] == "Delivery"
]

print("\n -- Vendas Realizadas Por Delivery -- ")
print(f"Quantidade De Vendas: {len(vendas_delivery)}")

# Dictionary Comprehension

precos_produtos = {
    produto["nome"]: produto["preco"]
    for produto in produtos
}

print("\n -- Preços Dos Produtos -- ")

for nome, preco in precos_produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

# Tupla com os canais de venda
canais_venda = ("Balcão", "Delivery")

print("\n -- Canais De Venda -- ")

for canal in canais_venda:
    print(canal)
