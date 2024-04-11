from Buses import *
from Estaciones import *

if __name__ == "__main__":

    def menu():
        ciudad = Ciudad()

        madrid = Estacion('M', 'Madrid')
        toledo = Estacion('T', 'Toledo')
        segovia = Estacion('S', 'Segovia')
        guadalajara = Estacion('G', 'Guadalajara')
        avila = Estacion('A', 'Avila')

        ciudad.add_estacion(madrid)
        ciudad.add_estacion(toledo)
        ciudad.add_estacion(segovia)
        ciudad.add_estacion(guadalajara)
        ciudad.add_estacion(avila)

        ciudad.add_ruta(madrid, toledo, 72.5)
        ciudad.add_ruta(madrid, guadalajara, 66.6)
        ciudad.add_ruta(madrid, segovia, 91.6)
        ciudad.add_ruta(avila, guadalajara, 171)
        ciudad.add_ruta(avila, madrid, 95)
        ciudad.add_ruta(avila, toledo, 160)
        ciudad.add_ruta(segovia, avila, 64.3)
        ciudad.add_ruta(segovia, guadalajara, 153)
        ciudad.add_ruta(segovia, toledo, 159)
        ciudad.add_ruta(toledo, segovia, 159)

        bus = Bus()

        print("Bienvenido al sistema de Bus Station")
        opcion = int(input("Ingrese entre estas opciones: \n"
                       "1. Listar todas las posibles rutas desde Madrid hasta la terminal Guadalajara\n"
                       "2. Simular un dia de trabajo\n"
                       "3. Cerrar sesion\n"))
        while opcion < 1 or opcion > 3:
            opcion = input("Ingrese SOLO entre estas opciones: \n"
                           "1. Listar todas las posibles rutas desde Madrid hasta la terminal Guadalajara\n"
                           "2. Simular un dia de trabajo\n"
                           "3. Cerrar sesion\n")
        if opcion == 1:
            ciudad.encontrar_todas_las_rutas('M', 'G')
            menu()
        elif opcion == 2:
            ciudad.agregar_pasajeros_manualmente()
            bus.definir_ruta2(bus, ciudad, madrid)
        elif opcion == 3:
            print("Gracias por usar Bus Station")

    menu()
