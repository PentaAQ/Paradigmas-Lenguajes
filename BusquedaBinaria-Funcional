def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


datos_ordenados = [5, 15, 25, 35, 45, 55]
print(busqueda_binaria(datos_ordenados, 35))
print(busqueda_binaria(datos_ordenados, 100))
