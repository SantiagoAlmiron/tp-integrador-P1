# Este es el algoritmo más básico para calcular si un número es primo o no.
# Vamos a definirlo en una función que recibe un número entero y devuelve True si es primo y False si no lo es.
# Luego vamos a construir una función que mida el tiempo que tarda en ejecutarse
from time import time
from math import isqrt

def optimized_is_prime(n):
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

def optimized_automatic_tests():
  # Casos para números no primos (4 casos, de menor a mayor)
  measure_time(optimized_is_prime, 10)
  measure_time(optimized_is_prime, 200)
  measure_time(optimized_is_prime, 4000)
  measure_time(optimized_is_prime, 200000)

  # Casos para números primos (10 casos, de menor a mayor)
  measure_time(optimized_is_prime, 104729)
  measure_time(optimized_is_prime, 1299709)
  measure_time(optimized_is_prime, 15485863)
  measure_time(optimized_is_prime, 32452843)
  measure_time(optimized_is_prime, 49979687)
  measure_time(optimized_is_prime, 67867967)
  measure_time(optimized_is_prime, 86028121)
  measure_time(optimized_is_prime, 104395303)
  measure_time(optimized_is_prime, 122949829)
  measure_time(optimized_is_prime, 141650939)
