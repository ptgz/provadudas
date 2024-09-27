def calcula_total_por_produto(transacoes):
    total_por_produto = {}
    for transacao in transacoes:
        produto = transacao["produto"]
        quantidade = transacao["quantidade"]
        preco_unitario = transacao["preco_unitario"]
        total = quantidade * preco_unitario
        if produto in total_por_produto:
            total_por_produto[produto] += total
        else:
            total_por_produto[produto] = total
    return total_por_produto
    

    
transacoes = [
    {"id": 1, "produto": "Camisa", "quantidade": 2, "preco_unitario": 50.0},
    {"id": 2, "produto": "Calça", "quantidade": 1, "preco_unitario": 100.0},
    {"id": 3, "produto": "Sapato", "quantidade": 1, "preco_unitario": 150.0},
    {"id": 4, "produto": "Camisa", "quantidade": 1, "preco_unitario": 50.0},
    {"id": 5, "produto": "Calça", "quantidade": 2, "preco_unitario": 100.0}
]

print(calcula_total_por_produto(transacoes))