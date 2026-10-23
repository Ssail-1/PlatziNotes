
import random

random.randrange(1, 10)  # Devuelve un número entero aleatorio entre 1 y 9
random.randrange(1, 10, 2)  # Devuelve un número entero aleatorio entre 1 y 9, con un paso de 2 (1, 3, 5, 7, 9)
random.randint(1, 10)  # Devuelve un número entero aleatorio entre 1 y 10
random.choice([1, 2, 3, 4, 5])  # Devuelve un elemento aleatorio de la lista
random.shuffle([1, 2, 3, 4, 5])  # Mezcla los elementos de la lista de forma aleatoria; OJO: no devuelve nada, modifica la lista original

# Con el módulo random también podemos generar números decimales aleatorios
random.random()  # Devuelve un número decimal aleatorio entre 0.0 y 1.0
random.uniform(1.5, 2.5)  # Devuelve un número decimal aleatorio entre 1.5 y 2.5

r = round(random.uniform(1.5, 2.5), 2)  # Devuelve un número decimal aleatorio entre 1.5 y 2.5, con 2 decimales

print(r)
