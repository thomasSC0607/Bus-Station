from Buses import *
from Estaciones import *

if __name__ == "__main__":
    ciudad = Ciudad()

    madrid = Estacion('M', 'Madrid', 8)
    toledo = Estacion('T', 'Toledo', 9)
    segovia = Estacion('S', 'Segovia', 10)
    guadalajara = Estacion('G', 'Guadalajara', 11)
    avila = Estacion('A', 'Avila', 12)

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

    ciudad.mostar_ciudad()

    bus = Bus()
    bus.definir_ruta(bus, ciudad, madrid)

