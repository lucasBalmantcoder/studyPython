# a, b, c = map(int, input().split())

# d, e, f = sorted([a, b, c])
# print(f"{d}\n{e}\n{f}\n")
# print(f"{a}\n{b}\n{c}")

valores = list(map(int, input().split()))
for v in sorted(valores): print(v)
print()
for v in valores: print(v)
