def busqueda_lineal(lista, objetivo, indice=0):
    # Si la lista esta vacia retornas -1
    if not lista:
        return -1
    
    # Si el primer elemento es el buscado-devolver índice actual
    if lista[0] == objetivo:
        return indice
    
    return busqueda_lineal(lista[1:], objetivo, indice + 1)


# Ejemplo
datos = [10, 20, 30, 40, 50]
print(busqueda_lineal(datos, 30))
print(busqueda_lineal(datos, 99))
