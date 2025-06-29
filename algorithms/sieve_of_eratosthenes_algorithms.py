# En este algoritmo vamos a usar el algoritmo de la criba de Eratóstenes para encontrar todos los números primos hasta un número dado.
from time import time
from math import isqrt

def sieve_of_eratosthenes(n):
    if n < 2:
        return 'No es primo'

    # Casos especiales para números pequeños
    if n == 2:
        return 'Es primo'
    if n % 2 == 0:
        return 'No es primo'

    # Creamos una lista (sieve) de tamaño n+1, inicializada en True, para marcar si un número es primo.
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Iteramos desde 2 hasta la raíz cuadrada de n.
    for number in range(2, isqrt(n) + 1):
        if sieve[number]:
            for multiple in range(number * number, n + 1, number):
                sieve[multiple] = False

    return 'Es primo' if sieve[n] else 'No es primo'

def measure_time(func, arg):
    start_time = time()
    result = func(arg)
    end_time = time()
    execution_time = end_time - start_time
    return print(f"Resultado: {result}, Tiempo de ejecución: {execution_time:.6f} segundos")

def sieve_automatic_tests():
    # Casos para números no primos (4 casos, de menor a mayor)
    measure_time(sieve_of_eratosthenes, 10)
    measure_time(sieve_of_eratosthenes, 200)
    measure_time(sieve_of_eratosthenes, 4000)
    measure_time(sieve_of_eratosthenes, 200000)

    # Casos para números primos (10 casos, de menor a mayor)
    measure_time(sieve_of_eratosthenes, 104729)
    measure_time(sieve_of_eratosthenes, 1299709)
    measure_time(sieve_of_eratosthenes, 15485863)
    measure_time(sieve_of_eratosthenes, 32452843)
    measure_time(sieve_of_eratosthenes, 49979687)
    measure_time(sieve_of_eratosthenes, 67867967)
    measure_time(sieve_of_eratosthenes, 86028121)
    measure_time(sieve_of_eratosthenes, 104395303)
    measure_time(sieve_of_eratosthenes, 122949829)
    measure_time(sieve_of_eratosthenes, 141650939)
