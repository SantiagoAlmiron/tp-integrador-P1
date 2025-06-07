from time import time

def is_prime(n):
    if n <= 1:
        return 'No es primo'
    for i in range(2, n):
        if n % i == 0:
            return 'No es primo'
    return 'Es primo'

def measure_time(func, arg):
    start_time = time()
    result = func(arg)
    end_time = time()
    execution_time = end_time - start_time
    return arg, execution_time # Devuelve lo mismo sin el print. 
    #return print(f"{arg} \t {execution_time:.3f}")

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

# measure_time(is_prime, 104729)      # Primo muy grande
# measure_time(is_prime, 1299709)     # Primo aún más grande
# measure_time(is_prime, 15485863)    # Primo enorme
# measure_time(is_prime, 32452843)    # Primo aún más enorme
# measure_time(is_prime, 49979687)    # Primo gigante
# measure_time(is_prime, 67867967)    # Primo colosal
# measure_time(is_prime, 86028121)    # Primo titánico
# measure_time(is_prime, 104395303)   # Primo monstruoso
# measure_time(is_prime, 122949829)   # Primo gigantesco
# measure_time(is_prime, 141650939)   # Primo descomunal