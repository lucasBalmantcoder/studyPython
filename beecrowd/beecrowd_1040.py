# entrada das notas
notas = list(map(float, input().split()))
media = sum(n * p for n, p in zip(notas, [2, 3, 4, 1])) / 10

print(f"Media: {media:.1f}")
if(media >= 7):
    print("Aluno aprovado.")
elif(media <= 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Aluno em exame.\nNota do exame: {exame:.1f}")
    final = (media + exame) / 2
    print("Aluno aprovado." if final >= 5.0 else "Aluno reprovado.")
    print(f"Media final: {final:.1f}")
    
    

