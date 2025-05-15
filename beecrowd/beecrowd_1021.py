value = float(input())
centavos = int(round(value * 100))

cedulas  = {
    10000: "R$ 100.00",
    5000: "R$ 50.00",
    2000: "R$ 20.00",
    1000: "R$ 10.00",
    500: "R$ 5.00",
    200: "R$ 2.00"
}

moedas = {
    100: "R$ 1.00",
    50: "R$ 0.50",
    25: "R$ 0.25",
    10: "R$ 0.10",
    5: "R$ 0.05",
    1: "R$ 0.01"
}

print("NOTAS:")
for valor_nota in sorted(cedulas.keys(), reverse=True):
    qtd = centavos // valor_nota
    centavos %= valor_nota
    print(f"{qtd} nota(s) de {cedulas[valor_nota]}")

print("MOEDAS:")
for valor_moeda in sorted(moedas.keys(), reverse=True):
    qtd = centavos // valor_moeda
    centavos %= valor_moeda
    print(f"{qtd} moeda(s) de {moedas[valor_moeda]}")