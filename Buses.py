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

    def definir_ruta(self, bus):
        ciudad_inicio = madrid
        while bus.capacidad <= self.capacidad:
            self.recoger_pasajeros(ciudad_inicio)
            destinos = []
            for ruta in ciudad.rutas:
                if ruta.estacion_inicio == ciudad_inicio:
                    destinos.append(ruta.estacion_destino)
                menor = self.capacidad
                for destino in destinos:
                    if destino.noPasajeros < menor:
                        menor = destino.noPasajeros
                for a in destinos:
                    if a.noPasajeros == menor:
                        ciudad_destino = a
            ciudad_inicio = ciudad_destino


if __name__ == "__main__":
    bus = Bus()
    bus.definir_ruta(bus)

