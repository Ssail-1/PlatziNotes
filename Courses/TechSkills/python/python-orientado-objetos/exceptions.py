class BibliotecaError(Exception):
    """Clase base para errores relacionados con la biblioteca."""
    pass

class TituloInvalidoError(BibliotecaError):
    """Excepción lanzada cuando se proporciona un título de libro inválido."""
    def __init__(self, titulo):
        self.titulo = titulo
        super().__init__(f"El libro con el titulo: '{titulo}' no es valido")

class usuario_no_encontrado(BibliotecaError):
    """Excepción lanzada cuando un usuario no es encontrado en la biblioteca."""
    def __init__(self, cedula):
        self.cedula = cedula
        super().__init__(f"Usuario con cédula '{cedula}' no encontrado en la biblioteca")

# tengo que implementar las siguientes excepciones: (Aunque en mi codigo ya no es necesario)

# class LibroNoDisponibleError(BibliotecaError):

# class LimitePrestamosError(BibliotecaError):