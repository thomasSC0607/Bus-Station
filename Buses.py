from Estaciones import *


class Bus:
    def __init__(self):
        self.pasajeros = []
        self.capacidad = 15

    def recoger_pasajeros(self, estacion):
        if len(self.pasajeros) + estacion.no_pasajeros <= self.capacidad:
            for i in range(estacion.no_pasajeros):
                self.pasajeros.append(f'pasajero {i}')
            estacion.no_pasajeros = 0
        else:
            pasajerosPorFuera = abs((len(self.pasajeros) + estacion.no_pasajeros) - self.capacidad)
            pasajerosParaBordar = abs(pasajerosPorFuera - estacion.no_pasajeros)
            for i in range(pasajerosParaBordar):
                self.pasajeros.append(f'pasajero {i}')
            estacion.no_pasajeros = pasajerosPorFuera

    def definir_ruta(self, bus, ciudad, ciudad_inicio):
        c_inicio = ciudad_inicio
        while len(bus.pasajeros) <= self.capacidad:
            if len(bus.pasajeros) == self.capacidad:
                break
            self.recoger_pasajeros(c_inicio)
            destinos = []
            for ruta in ciudad.rutas:
                if ruta.estacion_inicio == c_inicio:
                    destinos.append(ruta.estacion_destino)
            menor = self.capacidad
            for destino in destinos:
                if destino.no_pasajeros < menor:
                    menor = destino.no_pasajeros
            for a in destinos:
                if a.no_pasajeros == menor:
                    ciudad_destino = a
            self.definir_ruta(bus, ciudad, ciudad_destino)
        print("Devolviendose porque la capacidad esta al maximo")
        return


if __name__ == "__main__":
    bus = Bus()
    bus.definir_ruta(bus, madrid)

