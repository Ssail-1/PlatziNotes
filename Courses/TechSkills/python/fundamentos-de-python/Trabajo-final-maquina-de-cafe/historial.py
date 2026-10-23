
import os # El módulo os proporciona una forma de interactuar con el sistema operativo, incluyendo funciones para manejar archivos y directorios. En este caso, se utiliza para construir una ruta de archivo que sea compatible con diferentes sistemas operativos.
ARCHIVO_PEDIDOS = os.path.join(os.path.dirname(__file__), "historial_pedidos.txt") # os.path.dirname(__file__) devuelve el directorio donde se encuentra el archivo actual (historial.py), y os.path.join() se utiliza para construir la ruta completa al archivo "historial_pedidos.txt" de manera segura, independientemente del sistema operativo que se esté utilizando. Esto asegura que el archivo se cree o se lea en el mismo directorio donde se encuentra el script, evitando problemas de rutas relativas o absolutas.

def ver_historial():

    try:
        
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            
            pedidos = archivo.readlines()
            
            if not pedidos:
                raise FileNotFoundError("\nNo hay pedidos registrados en el historial.\n")
            else:
                print("\n||-----------------------------HISTORIAL DE PEDIDOS----------------------------||")
                for indice, pedido in enumerate(pedidos):

                    pedido_formateado = pedido.split(",")
                    fecha = pedido_formateado[0].strip().replace('"', '')
                    cafe = pedido_formateado[2].strip().replace('"', '')

                    print(f"|| {indice:<2} {fecha:<12} {cafe:<59} ||") # como funciona el formato: https://www.w3schools.com/python/ref_string_format.asp
                        
    except FileNotFoundError:
        print("//********************************WARNING******************************||")
        print("|| POSIBLES ALARMAS:                                                   ||")
        print("||          - Aún no hay pedidos registrados.                          ||")
        print("||          - El archivo 'historial_pedidos.txt' no se encuentra       ||")
        print("||            en el directorio actual.                                 ||")
        print("||---------------------------------------------------------------------||")
        print("|| Si el problema persiste, contacta al soporte técnico.              ||")
        print("||*********************************************************************//")
    except Exception as e:
        print("//********************************ERROR******************************||")
        print("|| Ocurrió un error al intentar leer el historial de pedidos.         ||")
        print(f"|| Detalles del error: {e}                                           ||")
        print("||---------------------------------------------------------------------||")
        print("|| Por favor, intenta nuevamente o contacta al soporte técnico.       ||")
        print("||*********************************************************************//")
    finally:
        print("||-----------------------------------------------------------------------------||\n")