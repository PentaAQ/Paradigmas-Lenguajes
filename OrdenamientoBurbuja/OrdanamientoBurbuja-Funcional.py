def burbuja(lista):
    if len(lista) <= 1:
        return lista

    def pasar_burbuja(lst):
        if len(lst) == 1:
            return lst
        primero, segundo = lst[0], lst[1]
        if primero > segundo:
            return [segundo] + pasar_burbuja([primero] + lst[2:])
        else:
            return [primero] + pasar_burbuja(lst[1:])

    pasada = pasar_burbuja(lista)
    return burbuja(pasada[:-1]) + [pasada[-1]]


nums = [5, 3, 8, 4, 2]
print(burbuja(nums)) 
