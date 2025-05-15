for i in range(0, 11):
    I = i / 5
    for j in range(1, 4):
        J = j + I
        # Verifica se I e J são inteiros
        i_str = f"{int(I)}" if I.is_integer() else f"{I:.1f}"
        j_str = f"{int(J)}" if J.is_integer() else f"{J:.1f}"
        print(f"I={i_str} J={j_str}")
