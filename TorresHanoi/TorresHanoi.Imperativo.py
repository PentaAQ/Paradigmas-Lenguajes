def torres_hanoi_imperativo(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover de {origen} a {destino}")
    else:
        torres_hanoi_imperativo(n - 1, origen, auxiliar, destino)
        print(f"Mover de {origen} a {destino}")
        torres_hanoi_imperativo(n - 1, auxiliar, destino, origen)

torres_hanoi_imperativo(3, "A", "C", "B")
