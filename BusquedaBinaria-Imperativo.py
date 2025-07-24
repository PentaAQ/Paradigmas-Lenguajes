def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:  
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo: 
            return medio
        elif lista[medio] > objetivo: 
            fin = medio - 1
        else: 
            inicio = medio + 1

    return -1 

datos_ordenados = [5, 15, 25, 35, 45, 55]
print(busqueda_binaria(datos_ordenados, 35)) 
print(busqueda_binaria(datos_ordenados, 100))
