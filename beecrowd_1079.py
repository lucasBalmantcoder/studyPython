n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())
    media = (a * 2 + b * 3 + c * 5) / 10 # cálcula a média ponderada
    print(f"{media:.1f}")