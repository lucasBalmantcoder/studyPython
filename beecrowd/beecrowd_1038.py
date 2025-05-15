precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# recebe o código e a quantidade
code, amount = map(int, input().split())

# verifica se o código existe na tabela
if code in precos:
    # calcula o total
    total = precos[code] * amount
    print(f'Total: R$ {total:.2f}')
else:
    print("Código inválido.")