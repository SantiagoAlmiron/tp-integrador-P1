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
    return arg, execution_time # Devuelve lo mismo sin el print.
    #return print(f"Resultado: {result}, Tiempo de ejecución: {execution_time:.10f} segundos")

def cambio_coma(arg, execution_time):
        tiempo_formateado= f"{execution_time:.3f}".replace(".",",")    
        return f"{arg}\t{tiempo_formateado}"

primos_grandes = [
    104729,
    1299709,
    15485863,
    32452843,
    49979687,
    67867967,
    86028121,
    104395303,
    122949829,
    141650939
]

for i in primos_grandes:
    arg, tiempo = measure_time(is_prime, i)
    resultado = cambio_coma(arg, tiempo)
    print(resultado)