from typing import Protocol
from abc import ABC, abstractmethod
from exceptions import TituloInvalidoError

class SolicitanteProtocol(Protocol):
    
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

class UsuarioBase(ABC):
    @abstractmethod
    def solicitar_libro(self):
        pass
    
    @abstractmethod
    def metodo_prueba(self):
        pass

class Usuario(UsuarioBase):
    
    def __init__(self, name, cedula):
        self.name = name
        self.cedula = cedula
        self.libros_prestados = []
    
    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Solicitud de libro '{titulo}' realizada"
    
    def devolver_libro(self, titulo, biblioteca):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            for libro in biblioteca.libros:
                if titulo.lower() == libro.titulo.lower():
                    libro.devolver()
                    return f"Libro '{titulo}' devuelto por {self.name}"
        else:
            return f"El libro '{titulo}' no se encuentra entre los prestados por {self.name}"
    
    def metodo_prueba(self):
        return "Metodo prueba para saber como funciona ABC"
    
class Estudiante(Usuario):
    
    def __init__(self, name, cedula, carrera):
        super().__init__(name, cedula)
        self.carrera = carrera
        self.limite_libros = 3
    
    # {'Estudiante': {'name': 'Juan Pérez', 'cedula': '2', 'libros_prestados': [], 'carrera': 'Gestion Empresarial', 'limite_libros': 3}}
    @classmethod
    def recrear_usuario(cls, name, cedula, libros_prestados, carrera):
        estudiante = cls(name=name, cedula=cedula, carrera=carrera)
        estudiante.libros_prestados = libros_prestados
        return estudiante

    def solicitar_libro(self, titulo, biblioteca):
        if not titulo:
            raise TituloInvalidoError(f"{titulo}")
        
        for libro in biblioteca.libros:
            if titulo.lower() == libro.titulo.lower():
                if len(self.libros_prestados) < self.limite_libros:
                    if libro.prestar():
                        self.libros_prestados.append(titulo)
                        return f"Solicitud de libro '{titulo}' realizada para el estudiante {self.name}"
                    else:
                        return f"El libro '{titulo}' no está disponible para préstamo" 
                else:
                    return f"El estudiante {self.name} ha alcanzado el límite de libros prestados"
        else:
            raise TituloInvalidoError(f"{titulo}")
    
class Profesor(Usuario):
    
    def __init__(self, name, cedula, departamento):
        super().__init__(name, cedula)
        self.departamento = departamento
        self.limite_libros = None
    
    # {'Profesor': {'name': 'Dr. Ana Gómez', 'cedula': '1', 'libros_prestados': [], 'departamento': 'Matematicas', 'limite_libros': None}}
    @classmethod
    def recrear_usuario(cls, name, cedula, libros_prestados, departamento):
        profesor = cls(name=name, cedula=cedula, departamento=departamento)
        profesor.libros_prestados = libros_prestados
        return profesor
    
    def solicitar_libro(self, titulo, biblioteca):
        if not titulo:
            raise TituloInvalidoError(f"{titulo}")
        
        for libro in biblioteca.libros:
            if titulo.lower() == libro.titulo.lower():
                if libro.prestar():
                    self.libros_prestados.append(titulo)
                    return f"Solicitud de libro '{titulo}' realizada para el profesor {self.name}"
                else:
                    return f"El libro '{titulo}' no está disponible para préstamo" 
        else:
            raise TituloInvalidoError(f"{titulo}")
