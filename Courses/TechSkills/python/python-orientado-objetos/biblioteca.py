from exceptions import usuario_no_encontrado

class Biblioteca:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []
        
    def libros_disponibles(self):
        return [
            libro
            for libro in self.libros
            if libro.cantidad_disponible > 0]
        
    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise usuario_no_encontrado(f"'{cedula}'")
    
    def generar_cedula(self):
        cedulas = []

        for usuario in self.usuarios:
            try:
                cedulas.append(int(usuario.cedula))
            except ValueError:
                pass

        if not cedulas:
            return "1"

        return str(max(cedulas) + 1)