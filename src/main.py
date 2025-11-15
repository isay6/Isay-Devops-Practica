
# main.py
# Punto de entrada para probar el sistema en consola.

from Services.Tienda_service import TiendaService

if __name__ == "__main__":
    # 1) Instancia del servicio
    tienda = TiendaService()

    # 2) Registrar al menos 3 clientes y 1 administrador
    cliente1 = tienda.registrar_usuario("cliente", "Isay",  "isay6@mail.com",  "Calle Jesús Soria 14")
    cliente2 = tienda.registrar_usuario("cliente", "Leo", "leonmarino@mail.com", "Calle Salvador Dalí 27")
    cliente3 = tienda.registrar_usuario("cliente", "India","indiamartinez@mail.com","Calle Galileo Galilei 17")
    admin = tienda.registrar_usuario("admin", "Admin", "admin@mail.com")

    # 3) Crear 5 productos de distintas categorías y añadirlos al inventario
    producto1 = tienda.anadir_producto("base",        "Libro",        10, 20)
    producto2 = tienda.anadir_producto("electronico", "Air Pods",     60, 10, garantia_meses=18)
    producto3 = tienda.anadir_producto("ropa",        "Sudadera",     50, 30, talla="M", color="Amarillo")
    producto4 = tienda.anadir_producto("base",        "Taza",         6, 50)
    producto5 = tienda.anadir_producto("ropa",        "Zapatos",      40, 15, talla="42", color="Negro")

    # 4) Listar productos para comprobar inventario
    print(" Inventario inicial ")
    for prod in tienda.listar_productos():
        print(prod)
    print()

    # 5) Simular 3 pedidos de distintos clientes con varios productos (fecha como string "YYYY-MM-DD")
    # Pedido 1 (Isay)
    items_1 = [(producto3.id, 2), (producto2.id, 1)]           # 2 Sudaderas, 1 Air Pods
    pedido1 = tienda.realizar_pedido(cliente1.id, items_1, "2025-09-16")

    # Pedido 2 (Leo)
    items_2 = [(producto1.id, 1), (producto4.id, 4), (producto3.id, 1)]  # 1 Libro, 4 Tazas, 1 Sudadera
    pedido2 = tienda.realizar_pedido(cliente2.id, items_2, "2025-04-16")

    # Pedido 3 (India)
    items_3 = [(producto5.id, 2), (producto1.id, 2)]           # 2 Zapatos, 2 Libros
    pedido3 = tienda.realizar_pedido(cliente3.id, items_3, "2025-01-07")

    # 6) Mostrar resumen de los pedidos y stock actualizado
    print(" Pedidos realizados ")
    for p in (pedido1, pedido2, pedido3):
        if p:
            print(p)  # __str__ del pedido (nombre cliente, fecha, total)
    print()

    print(" Stock actualizado tras los pedidos ")
    for prod in tienda.listar_productos():
        print(f"{prod.nombre} -> stock: {prod.stock}")
    print()

    # 7) Histórico de pedidos por orden de fecha de un cliente (ej.: Isay)
    print(" Histórico de pedidos de Isay (orden por fecha) ")
    historico_isay = tienda.listar_pedidos_por_fecha(cliente1.id)
    for p in historico_isay:
        print(p)
