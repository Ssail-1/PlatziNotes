
from asyncio import sleep
from datetime import datetime
ARCHIVO_PEDIDOS = "historial_pedidos.txt"


def pedir_cafe():
    while True:
        print('\n""""""""""""""""""""""""""""""""""""')  
        print("||  ¿Qué tipo de café desea?")
        print("||     1. Espresso")
        print("||     2. Latte")
        print("||     3. Cappuccino")
        print("||     4. Americano\n")

        tipo = int(input("|| Seleccione el tipo de café: -> "))

        cafes = {
            1: "Espresso",
            2: "Latte",
            3: "Cappuccino",
            4: "Americano"
        }

        if tipo in cafes:

            cafe_seleccionado = cafes[tipo]
            print("\n................................")
            print(f'''Ha seleccionado: {cafe_seleccionado}\n-> Preparando café... -\|/-\n''')

            with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
                fecha_hora = datetime.now().strftime('"%Y-%m-%d", "%H:%M:%S"') # El método strftime() se utiliza para formatear la fecha y hora actual en un formato específico. En este caso, se está formateando la fecha en el formato "YYYY-MM-DD" y la hora en el formato "HH:MM:SS", ambos entre comillas para que al escribirlos en el archivo se vean claramente separados del tipo de café.
                archivo.write(f'{fecha_hora}, "{cafe_seleccionado}"\n')
                # Esto agregará la fecha y hora del pedido en el formato "YYYY-MM-DD", "HH:MM:SS" seguido del tipo de café seleccionado para despues convertir el archivo en un formato csv y analizar los datos.
            return cafe_seleccionado   

        else:
            print("Opción no válida. Intentan de nuevo.")
