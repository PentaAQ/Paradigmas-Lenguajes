# Ejercicio de Fibonacci con paradigma funcional
def fibonacciFuncional(n):
    # 'n' representa el numero de fibonacci  en esa posicion
    if n <= 1:
        return n
    return fibonacciFuncional(n - 1) + fibonacciFuncional(n - 2)


print(fibonacciFuncional(10))
