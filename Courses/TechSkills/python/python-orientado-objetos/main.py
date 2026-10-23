from usuarios import *
from libros import *
from biblioteca import *
from exceptions import usuario_no_encontrado
from persistencia import Persistencia

# Ejecutable ---------------------------------------------------------------------------------------------------------------------------------- 
       
# Ahora si vamos en serio >:v

persistencia = Persistencia()

biblioteca = persistencia.cargar_datos()

def imprimir_datos_de_usuario_actual(usuario):
    print("||-------------------------------------------------------||")
    print(f"|| Usuario actual: {usuario.name}                       ")
    print(f"|| Cédula: {usuario.cedula}                             ")
    print(f"|| Libros prestados: {usuario.libros_prestados}         ")
    print(f"|| Usuario tipo: {type(usuario).__name__}               ")
    print("||-------------------------------------------------------||")
    
def ver_usuarios_registrados():
    print("||-------------------------------------------------------||")
    print("||           Usuarios registrados en la biblioteca       ||")
    print("||-------------------------------------------------------||")
    for usuario in biblioteca.usuarios:
        print(f"|| Nombre: {usuario.name}, Cédula: {usuario.cedula}, Usuario: {type(usuario).__name__} ||")
    print("||-------------------------------------------------------||")

def validacion_de_usuario():
    print("|| === }   Validacion de usuario              ||")
    cedula = input("|| Ingrese su cédula: ")
    try:
        usuario = biblioteca.buscar_usuario(cedula)
        return usuario
    except usuario_no_encontrado as e:
        print(f"{e}")
        nuevo_usuario = registrarUsuario()
        return nuevo_usuario

def valida_entrada_de_usuario(rango_inicial, rango_final):
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion >= rango_inicial) and (opcion <= rango_final):
                return int(opcion)
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

def registrarUsuario():
    print("*/* Deseas registrar nuevo usuario? 1. Si 2. NO")
    while True:
        opcion = valida_entrada_de_usuario(1,2)
        if opcion == 2:
            print()
            print("|| Sin usuario no se puede acceder a la biblioteca...    ||")
            return 4
        else:
            print()
            print("||           Registro de nuevo usuario                  ||")
            print("||-------------------------------------------------------||")
            name = input("Nombre: ")
            cedula = biblioteca.generar_cedula()
            print(f"Cédula asignada automáticamente: {cedula}")
            print("Tipo de usuario (1. estudiante || 2. profesor): ")
            tipo_usuario = valida_entrada_de_usuario(1,2)
            
            if tipo_usuario == 1:
                carrera = input("Ingrese la carrera del estudiante: ")
                nuevo_usuario = Estudiante(name, cedula, carrera)
            else:
                departamento = input("Ingrese el departamento del profesor: ")
                nuevo_usuario = Profesor(name, cedula, departamento)
            
            biblioteca.usuarios.append(nuevo_usuario)
            print(f"Usuario {name} registrado exitosamente.")
            return nuevo_usuario
        
def menuPrincipal():
    print("||-------------------------------------------------------||")
    print("|| 1. Solicitar libro                                    ||")
    print("|| 2. Devolver libro                                     ||")
    print("|| 3. Ver libros disponibles                              ||")
    print("|| 4. Agregar libros a la biblioteca                     ||")
    print("|| 5. Ver usuarios registrados                           ||")
    print("|| 6. Ver datos de usuario actual                        ||")
    print("|| 7. Modificar datos de usuario actual                  ||")
    print("|| 8. Cambiar de usuario                                  ||")
    print("|| 9. Modificar libro                                     ||")
    print("|| 0. Salir                                              ||")
    print("||-------------------------------------------------------||")
    opcion = valida_entrada_de_usuario(0, 9)
    return opcion

def ver_libros_disponibles():
    for i, libro in enumerate(biblioteca.libros_disponibles()):
        print(f"{i + 1}. - {libro.descripcion_de_libro}")
        print()

def solicitarLibro(biblioteca, usuario):
    print("||-------------------------------------------------------||")
    print("|| Lista de libros:")
    ver_libros_disponibles()
    titulo = input("Ingrese el título del libro que desea solicitar: ")
    while True:
        try:
            resultado = usuario.solicitar_libro(titulo, biblioteca)
            print(resultado)
            break
        except TituloInvalidoError as e:
            print(f"Error: {e}: {type(e)}")
            titulo = input("Ingrese un título válido: ")

def devolverLibro(biblioteca, usuario):
    print("||-------------------------------------------------------||")
    print("|| Lista de libros prestados:")
    for i, libro in enumerate(usuario.libros_prestados):
        print(f"{i + 1}. {libro}")
    titulo = input("Ingrese el título del libro que desea devolver: ")
    resultado = usuario.devolver_libro(titulo, biblioteca)
    print(resultado)

def agregar_libros(): 
    print("||-------------------------------------------------------||")
    print("||           Agregar libros a la biblioteca              ||")
    print("||-------------------------------------------------------||")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    while True:
        isbn = input("Ingrese el ISBN del libro: ")
        if isbn:
            if Libro.validar_isbn(isbn):
                break
            else:
                print("ISBN invalido, debe ser mayor igual a 10 (intente de nuevo)")
        else:
            print("isbn invalido, intenta de nuevo")
    cantidad_disponible = int(input("Ingrese la cantidad disponible del libro: "))
    
    while True:
        tipo_libro = input("Ingrese el tipo de libro (fisico/digital): ").strip().lower()
        if tipo_libro in ["fisico", "digital"]:
            break
        else:
            print("Tipo de libro inválido. Debe ser 'fisico' o 'digital'.")

    if tipo_libro == "fisico":
        nuevo_libro = LibroFisico(titulo, autor, isbn, cantidad_disponible)
    else:
        nuevo_libro = LibroDigital(titulo, autor, isbn, cantidad_disponible)
    
    biblioteca.libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado exitosamente a la biblioteca.")

def modificarUsuario(usuario):
    print("||-------------------------------------------------------||")
    print("||           Modificar datos de usuario                  ||")
    print("||-------------------------------------------------------||")
    print(f"Usuario actual: {usuario.name}, Cédula: {usuario.cedula}, Tipo: {type(usuario).__name__}")
    
    name = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ")
    # cedula = input("Ingrese la nueva cédula (dejar en blanco para no cambiar): ")
    
    if isinstance(usuario, Estudiante):
        carrera = input("Ingrese la nueva carrera (dejar en blanco para no cambiar): ")
        if carrera:
            usuario.carrera = carrera
    elif isinstance(usuario, Profesor):
        departamento = input("Ingrese el nuevo departamento (dejar en blanco para no cambiar): ")
        if departamento:
            usuario.departamento = departamento
    
    if name:
        usuario.name = name
    # if cedula:
    #     usuario.cedula = cedula
    
    print("Datos de usuario actualizados exitosamente.")

def modificarLibro():
    print("||-------------------------------------------------------||")
    print("|| Elige el titulo del libro a modificar:")
    for libro in biblioteca.libros:
        print(f"Cantidad: {libro.cantidad_disponible}, Veces prestado: {libro.veces_prestado}, Titulo: {libro.titulo}")
    titulo = input("\nIngresa el titulo del libro a modificar:")
    for libro in biblioteca.libros:
        if titulo.lower() == libro.titulo.lower():
            nuevo_titulo = input("Ingresa el nuevo titulo (deja en blanco para no cambiar):")
            if nuevo_titulo:
                libro.titulo = nuevo_titulo
            nuevo_autor = input("Ingresa el nuevo autor (deja en blanco para no cambiar):")
            if nuevo_autor:
                libro.autor = nuevo_autor
            
            while True:
                nuevo_isbn = input("Ingresa el nuevo isbn (deja en blanco para no cambiar):")
                if nuevo_isbn:
                    if Libro.validar_isbn(nuevo_isbn):
                        libro.isbn = nuevo_isbn
                        break
                    else:
                        print("ISBN invalido, debe ser mayor igual a 10 (intente de nuevo)")
                else:
                    break        
            nueva_cantidad_disponible = int(input("Ingresa la nueva cantidad disponible (deja en blanco para no cambiar):"))
            if nueva_cantidad_disponible:
                libro.cantidad_disponible = nueva_cantidad_disponible
            nueva_cantidad_de_veces_prestado = int(input("Cual es la cantidad de veces que fue prestado el libro? (deja en blanco para no cambiar):"))
            print(nueva_cantidad_de_veces_prestado)
            if nueva_cantidad_de_veces_prestado:
                libro.veces_prestado = nueva_cantidad_de_veces_prestado
            print("Libro actualizado con exito")
            print(libro.descripcion_de_libro)
            return True
    else:
        print("No se encontro el titulo (Intente de nuvo...)")
        return False

def sistema_principal(usuario):
    while True:
        print("||-------------------------------------------------------||")
        print(f"||    Bienvenido {usuario.name} a {biblioteca.nombre}    ||")

        opcion = menuPrincipal()
        
        # Doble validacion de usuario por si acaso
        try:
            biblioteca.buscar_usuario(usuario.cedula)
        except usuario_no_encontrado as e:
            print(f"{e}")
            print(f"Error {e}: VERIFIQUE REGISTRO DE USUARIO")
            imprimir_datos_de_usuario_actual(usuario)
            print("||-------------------------------------------------------||")
            ver_usuarios_registrados()

        match opcion:
            case 1:
                solicitarLibro(biblioteca, usuario)
            case 2:
                devolverLibro(biblioteca, usuario)
            case 3:
                ver_libros_disponibles()
            case 4:
                agregar_libros() 
            case 5:
                ver_usuarios_registrados()
            case 6:
                imprimir_datos_de_usuario_actual(usuario)
            case 7:
                modificarUsuario(usuario)
            case 8:
                return 8
            case 9:
                modificarLibro()
            case 0:
                print("||-------------------------------------------------------||")
                print("||           Gracias por usar la Biblioteca              ||")
                print("||-------------------------------------------------------||")
                break
        
        persistencia.guardar_datos(biblioteca)

# Inicia programa...
while True:
    usuario = validacion_de_usuario()
    if usuario == 4:
        print("||-------------------------------------------------------||")
        print("||           Gracias por usar la Biblioteca              ||")
        print("||-------------------------------------------------------||")
        break
    resultado = sistema_principal(usuario)
    if resultado == 8:
        continue # volvera a pedir usuario
    else:
        break
