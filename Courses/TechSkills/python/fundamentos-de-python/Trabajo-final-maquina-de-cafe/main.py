
from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():  
    while True:
        # Menu principal
        opcion = mostrar_menu()
        
        match opcion:
            case 1:
                print(f"{pedir_cafe()} listo, disfrútalo!")
                print("................................\n")
            case 2:
                # print("\nHistorial de pedidos:")
                # with open("historial_pedidos.txt", "r", encoding="utf-8") as archivo:
                #     for linea in archivo:
                #         print(linea.strip())
                ver_historial()
            case 0:
                print("\nGracias por usar la máquina de café. ¡Hasta luego!\n")
                break
            case _:
                print("Opción no válida. Ingrese una opción válida.")

# El bloque if __name__ == "__main__": se utiliza para asegurarse de que el código dentro de este bloque solo se ejecute cuando el script se ejecute directamente, y no cuando se importe como un módulo en otro script. Esto es útil para evitar que el código de prueba o de ejecución se ejecute accidentalmente cuando el script se importe en otro lugar.
if __name__ == "__main__":
    main()
