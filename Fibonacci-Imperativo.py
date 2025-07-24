def es_seguro(colocadas, fila, columna):
    # Verifica si es seguro poner una reina en (fila, columna)
    return all(
        columna != c and
        abs(columna - c) != fila - f
        for f, c in enumerate(colocadas)
    )

def resolver_n_reinas(n, fila=0, colocadas=()):
    # Si ya colocamos N reinas, devolvemos la solución
    if fila == n:
        return [colocadas]
    
    # Intentamos colocar una reina en cada columna posible
    return [
        solucion
        for columna in range(n)
        if es_seguro(colocadas, fila, columna)
        for solucion in resolver_n_reinas(n, fila + 1, colocadas + (columna,))
    ]

# ---- PROBAR ----
n = 4
soluciones = resolver_n_reinas(n)
for sol in soluciones:
    print(sol)
