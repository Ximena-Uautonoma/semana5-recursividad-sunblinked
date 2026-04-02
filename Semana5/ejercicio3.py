"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    fac = 1
    if n == 0:
        return 0
    for i in range(1, n + 1):
        fac *= i
    return fac


def factorial_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n * factorial_recursivo(n - 1)
    
x = int(input("ingrese num: "))
print(f"factorial ciclo: {factorial_ciclo(x)}")
print(f"factorial recursivo: {factorial_recursivo(x)}")