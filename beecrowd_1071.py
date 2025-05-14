x = int(input())
y = int(input())

menor = min(x, y)
maior = max(x, y)

soma = 0
for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma += i

print(soma)