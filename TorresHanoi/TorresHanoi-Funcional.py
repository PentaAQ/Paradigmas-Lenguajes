def torres_hanoi_funcional(n, origen, destino, auxiliar):
    if n == 1:
        return [(origen, destino)]
    
    return (
        torres_hanoi_funcional(n - 1, origen, auxiliar, destino) +
        [(origen, destino)] +
        torres_hanoi_funcional(n - 1, auxiliar, destino, origen)
    )

movimientos = torres_hanoi_funcional(3, "A", "C", "B")
for mov in movimientos:
    print(f"Mover de {mov[0]} a {mov[1]}")
