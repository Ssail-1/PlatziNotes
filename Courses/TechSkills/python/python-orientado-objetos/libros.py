from typing import Protocol

class LibroProtocol(Protocol):
    
    def prestar(self) -> str:
        """Metodo que debe implementar cualquier libro
        Para ser prestado"""
        ...
    
    def devolver(self) -> str:
        """Metodo que debe implementar cualquier libro
        Para ser devuelto"""
        ...
        
    def es_popular(self) -> bool:
        """Metodo que debe implementar cualquier libro
        Para determinar si es popular o no"""
        ...
    
    def calcular_duracion_prestamo(self) -> int:
        """Metodo que debe implementar cualquier libro para calcular la duración del préstamo"""
        ...

class Libro:
    
    def __init__(self, titulo, autor, isbn, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantidad_disponible = cantidad_disponible
        self.__veces_prestado = 0

    # 'libros': [{'titulo': '100 años de soledad', 'autor': 'Gabriel García Márquez', 'isbn': '0987654321', 'cantidad_disponible': 5, '_Libro__veces_prestado': 0},
    @classmethod
    def recrear_libro(cls, titulo, autor, isbn, cantidad_disponible, veces_prestado):
        libro = cls(titulo, autor, isbn, cantidad_disponible)
        libro.__veces_prestado = veces_prestado
        return libro
    
    def __str__(self):
        return f"Libro: {self.titulo} por {self.autor}, ISBN: {self.isbn}, Cantidad disponible: {self.cantidad_disponible}, Préstamos: {self.__veces_prestado}"
        
    def prestar(self):
        if self.cantidad_disponible > 0:
            self.cantidad_disponible -= 1
            self.__veces_prestado += 1
            return True
        else:
            return False
    
    def devolver(self):
        self.cantidad_disponible += 1
        return True
    
    def es_popular(self):
        return True if self.__veces_prestado > 5 else False
    
    @property
    def descripcion_de_libro(self):
        return f"""Titulo: {self.titulo}
    Autor: {self.autor}
    isbn: {self.isbn}
    Cantidad disponible: {self.cantidad_disponible}
    Veces prestado: {self.__veces_prestado}"""
    
    @property
    def veces_prestado(self):
        return self.__veces_prestado
    
    @veces_prestado.setter
    def veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado if veces_prestado >= 0 else self.__veces_prestado

    @staticmethod
    def validar_isbn(isbn):
        return len(isbn) >= 10
    
class LibroFisico(Libro):
        
    def calcular_duracion_prestamo(self):
        return "7 días"
    
class LibroDigital(Libro):
        
    def calcular_duracion_prestamo(self):
        return "14 días"
