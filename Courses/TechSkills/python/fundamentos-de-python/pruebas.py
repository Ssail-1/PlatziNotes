
if 5 > 3:
    print("5 es mayor que 3")

x = 5
y = 2

print(x % y == 0)  # False, porque el resto de dividir 5 entre 2 es 1, no 0

# Para que es isinstance() se use correctamente, debemos pasarle dos argumentos: el objeto que queremos verificar y el tipo de dato que queremos comprobar. Por ejemplo:
print(isinstance(x, int))  # True, porque x es un entero
print(isinstance(y, str))  # False, porque y es un entero, no una cadena

animales = ["Perro", "Gato", "Conejo", "Pollito"]

for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    print(type(num))  # <class 'tuple'>, porque num es una tupla que contiene el índice y el valor de cada elemento en la lista
    # Porque valor aumenta sin indicarle que aumente, el valor de indice aumenta automáticamente en cada iteración del bucle for, ya que enumerate() devuelve un objeto iterable que genera pares de índice y valor para cada elemento en la lista. Por lo tanto, no es necesario incrementar manualmente el índice, ya que enumerate() se encarga de eso por nosotros.
    # No entendí como funciona numerate, pero básicamente lo que hace es crear una tupla con el índice y el valor de cada elemento en la lista. Por ejemplo, en la primera iteración, num sería (0, "Perro"), en la segunda iteración sería (1, "Gato"), y así sucesivamente. Luego, podemos acceder al índice usando num[0] y al valor usando num[1].    

# Podemos también usar unpacking para hacer el código más limpio:
for indice, valor in enumerate(animales):
    print(type(indice), type(valor))  # <class 'int'>, <class 'str'>, porque indice es un entero y valor es una cadena
    print(f"El indice es: {indice} y el valor es: {valor}")
    
adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Banana", "Naranja", "Uva"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(f"{fruta} es {adjetivo}")

# Haz mas corto el código usando list comprehension:
[print(f"{fruta} es {adjetivo}") for fruta in frutas for adjetivo in adjetivos]

print("-" * 20)
