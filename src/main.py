import csv

produtos = []

with open("dados/produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for linha in leitor:
        produtos.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": float(linha[3])
        })


vendas = []

with open("dados/vendas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for linha in leitor:
        vendas.append({
            "id": linha[0],
            "cliente": linha[1],
            "produto": linha[2],
            "quantidade": int(linha[3]),
            "valor_total": float(linha[4]),
            "canal": linha[5]
        })


produtos_id = {}

for produto in produtos:
    produtos_id[produto["id"]] = produto


def faturamento_categoria(vendas):
    resultado = {}

    for venda in vendas:
        id_produto = venda["produto"]
        categoria = produtos_id[id_produto]["categoria"]

        if categoria not in resultado:
            resultado[categoria] = 0

        resultado[categoria] = resultado[categoria] + venda["valor_total"]

    return resultado


resultado = faturamento_categoria(vendas)

print("\n-- Faturamento Por Categoria --")

for categoria in resultado:
    print(categoria, ": R$", format(resultado[categoria], ".2f"))


def produtos_vendidos(vendas):
    quantidade = {}

    for venda in vendas:
        id_produto = venda["produto"]

        if id_produto not in quantidade:
            quantidade[id_produto] = 0

        quantidade[id_produto] = quantidade[id_produto] + venda["quantidade"]

    return quantidade


resultado = produtos_vendidos(vendas)

print("\n-- Produtos Mais Vendidos --")

for id_produto in resultado:
    nome = produtos_id[id_produto]["nome"]
    print(nome, ":", resultado[id_produto], "unidades")


def produto_mais_vendido(vendas):
    quantidade = {}

    for venda in vendas:
        id_produto = venda["produto"]

        if id_produto not in quantidade:
            quantidade[id_produto] = 0

        quantidade[id_produto] += venda["quantidade"]

    maior = 0
    produto_maior = ""

    for id_produto in quantidade:
        if quantidade[id_produto] > maior:
            maior = quantidade[id_produto]
            produto_maior = id_produto

    return produto_maior, maior


id_produto, quantidade = produto_mais_vendido(vendas)

print("\n-- Produto Mais Vendido --")
print(produtos_id[id_produto]["nome"], ":", quantidade, "unidades vendidas")


# clientes diferentes
clientes = set()

for venda in vendas:
    clientes.add(venda["cliente"])

print("\n-- Clientes Únicos --")
print("Quantidade de clientes diferentes:", len(clientes))
print(clientes)


# clientes do balcao
clientes_balcao = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Balcão"
}

# clientes do delivery
clientes_delivery = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Delivery"
}

clientes_dois_canais = clientes_balcao.intersection(clientes_delivery)

print("\n-- Clientes Que Compraram Nos Dois Canais --")
print(clientes_dois_canais)


# produtos com preço maior que 30
produtos_caros = [
    produto["nome"]
    for produto in produtos
    if produto["preco"] > 30
]

print("\n-- Produtos acima de R$ 30 --")

for nome in produtos_caros:
    print(nome)


# vendas delivery
vendas_delivery = [
    venda
    for venda in vendas
    if venda["canal"] == "Delivery"
]

print("\n-- Vendas Realizadas Por Delivery --")
print("Quantidade de vendas:", len(vendas_delivery))


# preços dos produtos
precos = {
    produto["nome"]: produto["preco"]
    for produto in produtos
}

print("\n-- Preços Dos Produtos --")

for nome in precos:
    print(nome, ": R$", format(precos[nome], ".2f"))


# tupla
canais = ("Balcão", "Delivery")

print("\n-- Canais De Venda --")

for canal in canais:
    print(canal)
