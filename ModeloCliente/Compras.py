from ModeloCliente.Clientes import *



class Compras:
    
    def __init__(self, NombreProducto, cantidad = 1, PrecioBase =0) -> None:
        self.NombreProducto = NombreProducto
        self.cantidad = cantidad
        self.PrecioBase = PrecioBase
            
    def TotalLineaCompra(self):

        return self.cantidad * self.PrecioBase
    

def RegistrarCompra(ListaProductos):
    suma = 0
    cuenta = 0
    for productos in ListaProductos:
        cuenta = cuenta + 1
        suma += productos.TotalLineaCompra()
    return suma, cuenta

