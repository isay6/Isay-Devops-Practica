
class Usuario:
    _siguiente_id = 1  # contador para IDs únicos

    def __init__(self, nombre, correo):
        self.id = Usuario._siguiente_id
        Usuario._siguiente_id += 1
        self.nombre = nombre
        self.correo = correo

    def is_admin(self):
        # por defecto siempre False
        return False

    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', correo='{self.correo}')"


class Cliente(Usuario):
    def __init__(self, nombre, correo, direccion):
        super().__init__(nombre, correo)
        self.direccion = direccion

    def __str__(self):
        return (f"Cliente(id={self.id}, nombre='{self.nombre}', correo='{self.correo}', "
                f"direccion='{self.direccion}')")


class Administrador(Usuario):
    def is_admin(self):
        # sobrescribe: devuelve True
        return True

    def __str__(self):
        return f"Administrador(id={self.id}, nombre='{self.nombre}', correo='{self.correo}')"
