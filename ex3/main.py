transacoes = [
    {"id": 1, "produto": "Camisa", "quantidade": 2, "preco_unitario": 50.0},
    {"id": 2, "produto": "Calça", "quantidade": 1, "preco_unitario": 100.0},
    {"id": 3, "produto": "Sapato", "quantidade": 1, "preco_unitario": 150.0},
    {"id": 4, "produto": "Camisa", "quantidade": 1, "preco_unitario": 50.0},
    {"id": 5, "produto": "Calça", "quantidade": 2, "preco_unitario": 100.0}
]

def calcula_total_por_produto(transacoes = transacoes):
    out = {}
    for item in transacoes:
        out[item['produto']] = item['quantidade'] * item['preco_unitario']

    return out


print(calcula_total_por_produto(transacoes))
    