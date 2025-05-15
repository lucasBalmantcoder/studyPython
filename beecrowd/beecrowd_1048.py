s = float(input())
p = 15 if s <= 400 else 12 if s <= 800 else 10 if s <= 1200 else 7 if s <= 2000 else 4
r = s * p / 100
print(f"Novo salario: {s + r:.2f}\nReajuste ganho: {r:.2f}\nEm percentual: {p} %")
