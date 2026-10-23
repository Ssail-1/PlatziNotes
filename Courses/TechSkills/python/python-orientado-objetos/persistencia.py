import json
from datetime import datetime

from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor
from libros import LibroDigital, LibroFisico

class Persistencia:
    
    def __init__(self, archivo = "biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [{
                "tipo_usuario": usuario.__class__.__name__,
                "datos_usuario": usuario.__dict__
                } for usuario in biblioteca.usuarios],
            "libros": [{
                "tipo_libro": libro.__class__.__name__,
                "datos_libro":libro.__dict__
                } for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat()
        }
        
        with open(self.archivo, 'w', encoding= 'UTF-8') as file:
            json.dump(datos, file, indent = 4, ensure_ascii=False)
            
    def cargar_datos(self):
        with open(self.archivo, "r", encoding= "UTF-8") as file:
            datos = json.load(file)
        
        biblioteca = Biblioteca(datos["nombre"])
        
        for usuario_guardado in datos["usuarios"]:
        
            tipo_usuario = usuario_guardado["tipo_usuario"]
            datos_de_usuario = usuario_guardado["datos_usuario"]
            
            if tipo_usuario == "Estudiante":
                usuario = Estudiante.recrear_usuario(
                    name=datos_de_usuario["name"],
                    cedula=datos_de_usuario["cedula"],
                    libros_prestados=datos_de_usuario["libros_prestados"],
                    carrera=datos_de_usuario["carrera"]
                )
            else: # es Profesor
                usuario = Profesor.recrear_usuario(
                    name=datos_de_usuario["name"],
                    cedula=datos_de_usuario["cedula"],
                    libros_prestados=datos_de_usuario["libros_prestados"],
                    departamento=datos_de_usuario["departamento"]
                )
            biblioteca.usuarios.append(usuario)
            
        for libro_guardado in datos["libros"]:
            tipo_libro = libro_guardado["tipo_libro"]
            datos_libro = libro_guardado["datos_libro"]
            
            if tipo_libro == "LibroFisico":
                libro_a_guardar = LibroFisico.recrear_libro(
                    titulo=datos_libro["titulo"],
                    autor=datos_libro["autor"],
                    isbn=datos_libro["isbn"],
                    cantidad_disponible=datos_libro["cantidad_disponible"],
                    veces_prestado=datos_libro["_Libro__veces_prestado"]
                )
            else:
                libro_a_guardar = LibroDigital.recrear_libro(
                    titulo=datos_libro["titulo"],
                    autor=datos_libro["autor"],
                    isbn=datos_libro["isbn"],
                    cantidad_disponible=datos_libro["cantidad_disponible"],
                    veces_prestado=datos_libro["_Libro__veces_prestado"]
                )
                pass
            biblioteca.libros.append(libro_a_guardar)
        
        return biblioteca