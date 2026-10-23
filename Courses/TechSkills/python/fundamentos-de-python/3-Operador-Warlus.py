
# OPERADOR WALRUS (:=)

# El operador walrus, representado por :=, es una adición a Python 3.8 que permite asignar valores a variables como parte de una expresión. Esto puede ser útil para evitar la repetición de código y mejorar la legibilidad.

# Ejemplo sin el operador walrus
n = len("Hola Mundo")
if n > 5:
    print(f"La longitud de la cadena es {n}, que es mayor que 5.")

# Ejemplo con el operador walrus
if (n := len("Hola Mundo")) > 5:
    print(f"La longitud de la cadena es {n}, que es mayor que 5.")

# En este ejemplo, el operador walrus nos permite calcular la longitud de la cadena y asignarla a la variable n dentro de la condición if, evitando la necesidad de calcularla por separado antes del if.