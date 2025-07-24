# Ejercicio de Fibonacci con paradigma imperativo

# 'n' representa el número de fibonacci en esa posición
n = 10

# Asignamos los valores iniciales
a = 0
b = 1

# Bucle para sumar los números anteriores
for _ in range(n):
    a, b = b, a + b

print(a)
