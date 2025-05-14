a, b, c, e = map(int, input().split())

inicio = a * 60 + b
fim = c * 60 + e

if fim <= inicio:
    fim += 24 * 60  # adiciona 24h em minutos

duracao = fim - inicio
horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
