
class Pedido:
    _siguiente_id = 1  # IDs únicos

    def __init__(self, cliente, fecha):
        self.id = Pedido._siguiente_id
        Pedido._siguiente_id += 1
        self.cliente = cliente          # objeto Cliente
        self.productos = []             # lista de (producto, cantidad)
        self.fecha = fecha              # string: "YYYY-MM-DD"

    def agregar_producto(self, producto, cantidad):
        # añade par (producto, cantidad)
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        # suma precio * cantidad
        return sum(prod.precio * cant for prod, cant in self.productos)

    def __str__(self):
        return (f"Pedido(id={self.id}, cliente='{self.cliente.nombre}', "
                f"fecha={self.fecha}, total={self.calcular_total():.2f} €)")

