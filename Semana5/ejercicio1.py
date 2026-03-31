"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""


def contar_ciclo(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    return lista
print(contar_ciclo(15))


def contar_recursivo(n):
    lista = []
    if n > 0:
        lista = contar_recursivo(n-1)
        lista.append(n)
        return lista
    else:
        return []
print("recursivo:", contar_recursivo(15))

# ojala me pesque el commit ahora.