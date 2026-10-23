
# open("ruta/al/archivo", "modo")

# Modos de apertura de archivos:
# "r" - Lectura (por defecto)
# "w" - Escritura (sobrescribe el archivo si ya existe)
# "a" - Escritura (agrega al final del archivo si ya existe)
# "x" - Creación (genera un error si el archivo ya existe)


# Antes de correrlo, la ruta en la terminal debe encontrarse al mismo nivel de este archivo .py o se creara el archivo en la ruta donde se encuentre la terminal, no en la ruta de este archivo .py

# Ejemplo de lectura de un archivo
try:
    with open("archivo.txt", "x") as archivo: # El modo "x" se utiliza para crear un nuevo archivo. Si el archivo ya existe, se generará un error FileExistsError.
        archivo.write("Este es un nuevo archivo creado con el modo 'x'.\n")
        archivo.write("Si intentamos crear el mismo archivo nuevamente, se generará un error.\n")
except FileExistsError:
    print("El archivo ya existe, no se puede crear nuevamente con el modo 'x'.")

try:    
    with open("archivo.txt", "r", encoding="utf-8") as archivo: # El bloque with se encarga de abrir el archivo y cerrarlo automáticamente al finalizar, incluso si ocurre un error durante la lectura.
        contenido = archivo.read() # El método read() lee todo el contenido del archivo y lo almacena en la variable "contenido". Si el archivo es muy grande, esto podría consumir mucha memoria, por lo que también existen otros métodos como readline() para leer línea por línea o readlines() para obtener una lista de todas las líneas del archivo.
        print(contenido)
        
    # tsss, esta aburrido esto, vamos a escribir algo en el archivo
    with open("archivo.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Hola, este es un nuevo contenido para el archivo.\n") # El método write() escribe el texto proporcionado en el archivo. Si el modo es "w", se sobrescribirá el contenido existente. Si el modo es "a", se agregará al final del archivo.
        archivo.write("Esta es otra línea de texto.\n")
    
    # Ahora vamos a leer el archivo nuevamente para ver el nuevo contenido
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        nuevo_contenido = archivo.readlines() # El método readlines() lee todas las líneas del archivo y las devuelve como una lista de cadenas, donde cada cadena representa una línea del archivo, incluyendo el carácter de nueva línea al final de cada línea.s
        for linea in nuevo_contenido:
            print(linea.strip()) 
    
    with open("archivo.txt", "a", encoding="utf-8") as archivo: # El modo "a" se utiliza para agregar contenido al final del archivo sin sobrescribirlo. Si el archivo no existe, se creará automáticamente.
        archivo.write("Agregando una nueva línea al final del archivo.\n")
        archivo.write("Otra línea más para demostrar el modo 'a'.\n")
        
    lineas_para_escribir = ["Primera línea escrita con writelines().\n", "Segunda línea escrita con writelines().\n", "Tercera línea escrita con writelines().\n"]
    with open("archivo.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas_para_escribir) # El método writelines() toma una lista de cadenas y las escribe en el archivo sin agregar automáticamente caracteres de nueva línea, por lo que es importante incluir el carácter de nueva línea "\n" al final de cada cadena si se desea que cada línea se escriba en una nueva línea del archivo.   
    
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        contenido_final = archivo.read()
        print(contenido_final)
except FileNotFoundError:
    print("El archivo no existe")