# Érase una vez un algoritmo en Python
# Este cuento narra la historia de un número que quería ser el doble de sí mismo

def cuento_del_numero(numero):
  """
  Un número soñaba con duplicarse.
  Así que pidió ayuda a una función mágica.
  """
  # El número se presenta ante la función
  print(f"Había una vez un número llamado {numero}.")

  # La función le concede el deseo de duplicarse
  doble = numero * 2
  print(f"Un día, decidió duplicarse y se convirtió en {doble}.")

  # El número vive feliz siendo el doble de lo que era
  print(f"Desde entonces, {numero} y {doble} vivieron felices, multiplicando su valor por el mundo.")
  return doble

# Fin del cuento
# Probemos el cuento con el número 7
if __name__ == "__main__":
  cuento_del_numero(7)
