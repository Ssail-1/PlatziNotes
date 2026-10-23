
# Sintaxis basica de manejo de errores en Python
try:
    # Código que puede generar un error
    resultado = 10 / 0  # Esto generará un error de división por cero1

except ZeroDivisionError: # Esto captura específicamente el posible error que podemos esperar, en este caso, el error de división por cero.
    
    # Código que se ejecuta si ocurre un error de división por cero
    print("No se puede dividir por cero")

except Exception as e: # Esto captura en "Exception" cualquier otro tipo de error que no sea ZeroDivisionError y lo asigna a la variable "e" para que podamos imprimirlo o manejarlo de alguna manera.
    
    # Código que se ejecuta si ocurre cualquier otro tipo de error
    print(f"Ocurrió un error: {e}")

else:
    # Código que se ejecuta si no ocurre ningún error
    print(f"El resultado es: {resultado}")
    
finally:
    # Código que se ejecuta siempre, independientemente de si ocurrió un error o no
    print("Este bloque se ejecuta siempre")