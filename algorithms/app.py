is_running = True

while is_running:
    # Limpiar la consola para una mejor visualización
    print("Seleccione el algoritmo a ejecutar:")
    print("1. Algoritmo básico de primalidad")
    print("2. Algoritmo optimizado ")
    print("3. Pruebas automáticas de todos los algoritmos")
    print("4. Salir")

    choice = input("Ingrese su elección (1/2/3): ")

    if choice == '1':
      from basic_algorithms import measure_time, is_prime
      number = int(input("Ingrese un número para verificar si es primo: "))
      measure_time(is_prime, number)
    elif choice == '2':
      from second_optimized_algorithms import measure_time, optimized_is_prime
      number = int(input("Ingrese un número para verificar si es primo: "))
      measure_time(optimized_is_prime, number)
    elif choice == '3':
      from sieve_of_eratosthenes_algorithms import sieve_automatic_tests
      from basic_algorithms import basic_automatic_tests
      from second_optimized_algorithms import optimized_automatic_tests

      print("Ejecutando pruebas automáticas del algoritmo básico...")
      basic_automatic_tests()
      print("\n")
      print("Ejecutando pruebas automáticas del algoritmo optimizado...")
      optimized_automatic_tests()
      print("\n")
      print("Ejecutando pruebas automáticas de la Criva...")
      sieve_automatic_tests()
    elif choice == '4':
      is_running = False
    else:
      print("Opción no válida. Intente de nuevo.")

    print("\n")  # Salto de línea para separar las iteraciones
