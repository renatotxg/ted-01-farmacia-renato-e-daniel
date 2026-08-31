```python
import csv


# Funcao para ler os produtos
def carregar_produtos():
    produtos = []

    try:
        with open("dados/produtos.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            for linha in leitor:
                if len(linha) >= 4:
                    produto = {
                        "id": linha[0],
                        "nome": linha[1],
                        "categoria": linha[2],
                        "preco": float(linha[3])
                    }

                    produtos.append(produto)

    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")

    return produtos


# Funcao para ler as vendas
def carregar_vendas():
    vendas = []

    try:
        with open("dados/vendas.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            for linha in leitor:
                if len(linha) >= 6:
                    venda = {
                        "id": linha[0],
                        "cliente": linha[1],
                        "produto": linha[2],
                        "quantidade": int(linha[3]),
                        "valor_total": float(linha[4]),
                        "canal": linha[5]
                    }

                    vendas.append(venda)

    except FileNotFoundError:
        print("Arquivo de vendas não encontrado.")

    return vendas


produtos = carregar_produtos()
vendas = carregar_vendas()


# Organizando os produtos pelo ID
produtos_por_id = {}

for produto in produtos:
    produtos_por_id[produto["id"]] = produto


def faturamento_categoria(vendas, produtos_por_id):
    faturamento = {}

    for venda in vendas:
        id_produto = venda["produto"]

        if id_produto in produtos_por_id:
            categoria = produtos_por_id[id_produto]["categoria"]

            if categoria not in faturamento:
                faturamento[categoria] = 0

            faturamento[categoria] += venda["valor_total"]

    return faturamento


resultado = faturamento_categoria(vendas, produtos_por_id)

print("\n================================")
print("     FATURAMENTO POR CATEGORIA")
print("================================")

# Ordenando as categorias pelo faturamento
categorias_ordenadas = sorted(
    resultado.items(),
    key=lambda x: x[1],
    reverse=True
)

for categoria, valor in categorias_ordenadas:
    print(f"{categoria}: R$ {valor:.2f}")


def produtos_mais_vendidos(vendas, produtos_por_id):
    quantidade_produtos = {}

    for venda in vendas:
        id_produto = venda["produto"]

        if id_produto not in quantidade_produtos:
            quantidade_produtos[id_produto] = 0

        quantidade_produtos[id_produto] += venda["quantidade"]

    return quantidade_produtos


resultado_produtos = produtos_mais_vendidos(vendas, produtos_por_id)

print("\n================================")
print("       PRODUTOS MAIS VENDIDOS")
print("================================")

produtos_ordenados = sorted(
    resultado_produtos.items(),
    key=lambda x: x[1],
    reverse=True
)

for id_produto, quantidade in produtos_ordenados:
    if id_produto in produtos_por_id:
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

    produto_id_mais_vendido = None
    maior_quantidade = 0

    for produto_id in quantidade_por_produto:
        if quantidade_por_produto[produto_id] > maior_quantidade:
            maior_quantidade = quantidade_por_produto[produto_id]
            produto_id_mais_vendido = produto_id

    if produto_id_mais_vendido in produtos_por_id:
        nome_produto = produtos_por_id[produto_id_mais_vendido]["nome"]
    else:
        nome_produto = "Produto não encontrado"

    return nome_produto, maior_quantidade


produto, quantidade = produto_mais_vendido(vendas, produtos_por_id)

print("\n================================")
print("         PRODUTO MAIS VENDIDO")
print("================================")
print(f"{produto}: {quantidade} unidades vendidas")


# Conjunto de clientes unicos
clientes_unicos = set()

for venda in vendas:
    clientes_unicos.add(venda["cliente"])

print("\n================================")
print("          CLIENTES UNICOS")
print("================================")
print(f"Quantidade de clientes diferentes: {len(clientes_unicos)}")
print(clientes_unicos)


# Clientes do balcao
clientes_balcao = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Balcão"
}

# Clientes do delivery
clientes_delivery_set = {
    venda["cliente"]
    for venda in vendas
    if venda["canal"] == "Delivery"
}

clientes_ambos = clientes_balcao.intersection(clientes_delivery_set)

print("\n================================")
print("      CLIENTES NOS DOIS CANAIS")
print("================================")
print(clientes_ambos)


# Produtos com preco acima de 30
produtos_caros = [
    produto["nome"]
    for produto in produtos
    if produto["preco"] > 30
]

print("\n================================")
print("       PRODUTOS ACIMA DE R$ 30")
print("================================")

for produto in produtos_caros:
    print(produto)


# Vendas realizadas por delivery
vendas_delivery = [
    venda
    for venda in vendas
    if venda["canal"] == "Delivery"
]

print("\n================================")
print("        VENDAS POR DELIVERY")
print("================================")
print(f"Quantidade de vendas: {len(vendas_delivery)}")


# Dictionary comprehension
precos_produtos = {
    produto["nome"]: produto["preco"]
    for produto in produtos
}

print("\n================================")
print("          PRECOS DOS PRODUTOS")
print("================================")

for nome, preco in precos_produtos.items():
    print(f"{nome}: R$ {preco:.2f}")


# Tupla com os canais de venda
canais_venda = ("Balcão", "Delivery")

print("\n================================")
print("           CANAIS DE VENDA")
print("================================")

for canal in canais_venda:
    print(canal)


# Faturamento total
faturamento_total = 0

for venda in vendas:
    faturamento_total += venda["valor_total"]


# Quantidade total de produtos vendidos
quantidade_total = 0

for venda in vendas:
    quantidade_total += venda["quantidade"]


# Relatorio final
print("\n================================")
print("          RELATORIO FINAL")
print("================================")

print(f"Quantidade de produtos cadastrados: {len(produtos)}")
print(f"Quantidade de vendas: {len(vendas)}")
print(f"Clientes unicos: {len(clientes_unicos)}")
print(f"Produtos vendidos: {quantidade_total}")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Produto mais vendido: {produto}")
print(f"Quantidade vendida: {quantidade}")
```
