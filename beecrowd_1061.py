dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))


dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))


inicio_total = dia_inicio * 86400 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
fim_total = dia_fim * 86400 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim


duracao = fim_total - inicio_total

dias = duracao // 86400
duracao %= 86400
horas = duracao // 3600
duracao %= 3600
minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")