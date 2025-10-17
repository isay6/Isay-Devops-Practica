class Producto:
    _siguiente_id = 1

    def __init__(self, nombre, precio, stock):
        self.id = Producto._siguiente_id
        Producto._siguiente_id += 1
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad):
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            # devolvemos False para indicar que no se pudo hacer
            print("No puedes vender más de lo que hay en stock.")
            return False
        else:
            self.stock = nuevo_stock
            return True

    def __str__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio:.2f}, stock={self.stock})"



class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def __str__(self):
        return (f"ProductoElectronico(id={self.id}, nombre='{self.nombre}', "
                f"precio={self.precio:.2f}, stock={self.stock}, garantia_meses={self.garantia_meses})")


class ProductoRopa(Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self):
        return (f"ProductoRopa(id={self.id}, nombre='{self.nombre}', "
                f"precio={self.precio:.2f}, stock={self.stock}, talla='{self.talla}', color='{self.color}')")
