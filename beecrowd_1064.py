positivos = 0  
media = 0
for _ in range(6):
    valor = float(input())
    if valor > 0:  
        media += valor
        positivos += 1 
        
print(f"{positivos} valores positivos")
print(f"{media/positivos:.1f}")
