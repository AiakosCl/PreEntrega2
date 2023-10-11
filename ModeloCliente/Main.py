# Importa la clase Cliente y la función CrearCliente desde el módulo cliente.py
from ModeloCliente.Clientes import Clientes, BuscarCliente, CrearCliente
from ModeloCliente.Compras import Compras, RegistrarCompra
import os, time as t, keyboard as k, json as j

def limpiar():
    if os.name == "nt":
        os.system("CLS")
    else:
        os.system("clear")



# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    limpiar()
    print("Menú:\n")
    print("1. Crear un nuevo cliente.")
    print("2. Ver información del cliente.")
    print("3. Mostrar Venta.")
    print("4. Salir.")
    opcion = input("\n\tElija una opción (1/2/3/4): ")
    return opcion

# Función principal
def main():

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            # Opción para crear un nuevo cliente. Dejará de ingresar clientes, sólo cuando se de <Enter> sin datos.
            
            while True:
                limpiar()
                
                
                print("Ingrese los datos del cliente: \n")
                

                DatoCliente = {
                    "Nombre": input("Nombre Completo\t\t:\t"),
                    "Correo": input("Correo electrónico\t:\t"),
                    "Telefono": input("Número de Telefóno\t:\t"),
                    "Direccion": input("Dirección legal\t\t:\t")
                }
                
                NuevoCliente = CrearCliente(DatoCliente)
                

                print("\n**Cliente creado exitosamente.**")
                respuesta = input("\n\t¿Desea agregar a otro cliente (S/N)?").upper()
                if respuesta == "N" or not respuesta:
                    break

            
        elif opcion == "2":
            # Opción 2: Se buscará al cliente por su correo y se mostrará su información si se encuentra
            limpiar()
            Busqueda = input("Ingrese el correo de cliente que se busca: ").lower()
            
            Registro = BuscarCliente(Busqueda)
            limpiar()
            
            if Registro:
                print("Datos del cliente: \n")
                print(f"Nombre Completo\t\t:\t{Registro['Nombre']}")
                print(f"Correo electrónico\t:\t{Registro['Correo']}.")
                print(f"Teléfono\t\t:\t{Registro['Telefono']}.")
                print(f"Dirección\t\t:\t{Registro['Direccion']}.")
            
            else:
                print("No se ha encontrado al cliente con ese e-mail")
        
            print("\nPresione <esc> para continuar...")
            k.wait('esc')

        elif opcion == "3":
            # Opción 3: Se simula una compra
            ListaProductos = [
                Compras("Televisor",2,3000),
                Compras("Computador",1,5000),
                Compras("Hervidor",1,1000)
            ]
            
            limpiar()
            print(f"Se han comprado {RegistrarCompra(ListaProductos)[1]}, por un total de: ${RegistrarCompra(ListaProductos)[0]}.\n\n")
            print("\nPresione <esc> para continuar...")
            k.wait("esc")

        elif opcion == "4":
            # Opción 4: Salir del programa
            print("\nSaliendo del programa.")
            t.sleep(1)
            limpiar()
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
