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
            "preco": float(linha[3],)
            
        }
        produtos.append(produto)
print(produtos)


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
print(vendas)