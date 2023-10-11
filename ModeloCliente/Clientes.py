
import datetime as dt
import json as j, os


class Clientes:
    
    def __init__(self, DatosCliente) -> None:
        
        self.Nombre = DatosCliente["Nombre"]
        self.correo = DatosCliente ["Correo"]
        self.telefono = DatosCliente["Telefono"]
        self.direccion = DatosCliente["Direccion"]
        self.NuevoCliente = DatosCliente

def CrearCliente(NuevoCliente):

    try:
        NombreArchivo = os.path.dirname(__file__)+"\Clientes.json"

        with open(NombreArchivo,"a") as BaseCliente:
            j.dump(NuevoCliente, BaseCliente)
            BaseCliente.write("\n")
            print(f"\nSe ha creado al cliente: {NuevoCliente['Nombre']}.")
    
    except FileNotFoundError:
        CrearArchivo = input("\nEl Archivo de base de datos Clientes, no existe ¿Desea crearlo (S/N)? ").upper()
        if CrearArchivo == "S":
            NombreArchivo = os.path.dirname(__file__)+"\Clientes.json"
            print(NombreArchivo)
            with open(NombreArchivo, "w") as BaseCliente:
                j.dump(NuevoCliente, NombreArchivo, indent=4)
                
            print(f"Se ha creado la base: {NombreArchivo}.")
        else:
            ...

def BuscarCliente(CorreoClave):
    
    try:
        with open(os.path.dirname(__file__)+"\Clientes.json","r") as BaseCliente:
            datos = BaseCliente.readlines() 
    
        for registro in datos:
            DatosRegistro = j.loads(registro)
            if DatosRegistro["Correo"] == CorreoClave:
                return DatosRegistro
        # return None
    except FileNotFoundError:
        return None
