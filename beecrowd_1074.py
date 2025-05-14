# Lê o número de casos de teste
N = int(input())

for _ in range(N):
    X = int(input())
    
    if X == 0:
        print("NULL")
    else:
        tipo = "EVEN" if X % 2 == 0 else "ODD"
        sinal = "POSITIVE" if X > 0 else "NEGATIVE"
        print(f"{tipo} {sinal}")