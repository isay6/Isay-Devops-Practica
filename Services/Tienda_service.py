# Imports del modelo (clases que usa el servicio)
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Usuario import Usuario, Cliente, Administrador
from models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        self.usuarios = {}   # id -> Usuario
        self.productos = {}  # id -> Producto
        self.pedidos = {}    # id -> Pedido

    # registra Usuario según tipo: "cliente" o "admin"
    def registrar_usuario(self, tipo, nombre, correo, direccion=None):
        if tipo == "cliente":
            u = Cliente(nombre, correo, direccion)
        elif tipo == "admin":
            u = Administrador(nombre, correo)
        else:
            return None
        self.usuarios[u.id] = u
        return u

    # añade productos según categoría: "base", "electronico", "ropa"
    def anadir_producto(self, categoria, nombre, precio, stock, **extras):
        if categoria == "base":
            p = Producto(nombre, precio, stock)
        elif categoria == "electronico":
            p = ProductoElectronico(nombre, precio, stock, extras.get("garantia_meses", 0))
        elif categoria == "ropa":
            p = ProductoRopa(nombre, precio, stock, extras.get("talla", ""), extras.get("color", ""))
        else:
            return None
        self.productos[p.id] = p
        return p

    # elimina producto por id
    def eliminar_producto(self, producto_id):
        return self.productos.pop(producto_id, None)

    # lista todos los productos disponibles
    def listar_productos(self):
        return list(self.productos.values())

    # realiza pedido si existe el usuario (Cliente) y hay stock suficiente en todos los items
    # items = lista de tuplas (producto_id, cantidad)
    def realizar_pedido(self, usuario_id, items, fecha):
        usuario = self.usuarios.get(usuario_id)
        if not usuario or not isinstance(usuario, Cliente):
            return None

        # validar existencia y stock sin modificar nada
        productos_cant = []
        for pid, cant in items:
            prod = self.productos.get(pid)
            if not prod or not prod.hay_stock(cant):
                return None
            productos_cant.append((prod, cant))

        # crear pedido y descontar stock
        pedido = Pedido(usuario, fecha)
        for prod, cant in productos_cant:
            pedido.agregar_producto(prod, cant)
            prod.actualizar_stock(-cant)  # descuenta

        self.pedidos[pedido.id] = pedido
        return pedido

    # lista pedidos de un usuario por orden de fecha (YYYY-MM-DD)
    def listar_pedidos_por_fecha(self, usuario_id):
        user_pedidos = [p for p in self.pedidos.values() if p.cliente.id == usuario_id]
        return sorted(user_pedidos, key=lambda p: p.fecha)
