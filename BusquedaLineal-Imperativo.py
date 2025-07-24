def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)): 
        if lista[i] == objetivo: 
            return i 
    return -1 


# Ejemplo
datos = [10, 20, 30, 40, 50]
print(busqueda_lineal(datos, 30))  # Salida: 2
print(busqueda_lineal(datos, 99))  # Salida: -1
