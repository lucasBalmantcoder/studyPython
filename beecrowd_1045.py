a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    a2, b2, c2 = a**2, b**2, c**2
    if a2 == b2 + c2:
        print("TRIANGULO RETANGULO")
    elif a2 > b2 + c2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
