
# Casteo de Datos booleanos

# El numero 0 es considerado False, cualquier otro número es considerado True
print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True

# Strings vacíos son False, cualquier otro string es True
print(bool("Hola"))  # True
print(bool(""))  # False

# Listas vacías son False, cualquier otra lista es True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# None es considerado False; None => "Nada", "Vacío", "Null", "Ausencia de valor"
print(bool(None))  # False
