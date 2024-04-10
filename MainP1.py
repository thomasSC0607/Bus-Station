from Estaciones import *

if __name__ == "__main__":
    ciudad = Ciudad()

    madrid = Estacion('M', 'Madrid', 0)
    toledo = Estacion('T', 'Toledo', 0)
    segovia = Estacion('S', 'Segovia', 0)
    guadalajara = Estacion('G', 'Guadalajara', 0)
    avila = Estacion('A', 'Avila', 0)

    ciudad.add_estacion(madrid)
    ciudad.add_estacion(toledo)
    ciudad.add_estacion(segovia)
    ciudad.add_estacion(guadalajara)
    ciudad.add_estacion(avila)

    ciudad.add_ruta(madrid, toledo, 72.5)
    ciudad.add_ruta(madrid, segovia, 91.6)
    ciudad.add_ruta(toledo, segovia, 159)
    ciudad.add_ruta(segovia, avila, 64.3)
    ciudad.add_ruta(segovia, guadalajara, 153)
    ciudad.add_ruta(avila, guadalajara, 171)
    ciudad.add_ruta(madrid, guadalajara, 66.6)

    ciudad.mostar_ciudad()

    # Encuentra todas las rutas desde Madrid ('M') a Toledo ('T')
    ciudad.encontrar_todas_las_rutas('M', 'G')