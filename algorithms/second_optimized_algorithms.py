# Este es el algoritmo más básico para calcular si un número es primo o no.
# Vamos a definirlo en una función que recibe un número entero y devuelve True si es primo y False si no lo es.
# Luego vamos a construir una función que mida el tiempo que tarda en ejecutarse
from time import time
from math import isqrt

def is_prime(n):
  if n <= 1:
    return 'No es primo'
  if n == 2:
    return 'Es primo'
  if n % 2 == 0:
    return 'No es primo'
  square_root = isqrt(n)
  # Comenzamos a verificar desde 3 hasta la raíz cuadrada del número, solo con impares (por eso el paso es de 2),
  # ya que los pares ya fueron descartados antes.
  for i in range(3, square_root + 1, 2):
    if n % i == 0:
      return 'No es primo'
  return 'Es primo'

def measure_time(func, arg):
    start_time = time()
    result = func(arg)
    end_time = time()
    execution_time = end_time - start_time
    return print(f"Resultado: {result}, Tiempo de ejecución: {execution_time:.6f} segundos")

# Casos para números no primos (4 casos, de menor a mayor)
measure_time(is_prime, 10)      # No primo pequeño
measure_time(is_prime, 200)     # No primo mediano
measure_time(is_prime, 4000)    # No primo grande
measure_time(is_prime, 200000)  # No primo muy grande

# Casos para números primos (10 casos, de menor a mayor)
measure_time(is_prime, 3)         # Primo pequeño
measure_time(is_prime, 7)         # Primo pequeño
measure_time(is_prime, 29)        # Primo pequeño
measure_time(is_prime, 101)       # Primo mediano
measure_time(is_prime, 307)       # Primo mediano
measure_time(is_prime, 1009)      # Primo grande
measure_time(is_prime, 5003)      # Primo grande
measure_time(is_prime, 104729)    # Primo muy grande
measure_time(is_prime, 1299709)   # Primo aún más grande
measure_time(is_prime, 15485863)  # Primo enorme
