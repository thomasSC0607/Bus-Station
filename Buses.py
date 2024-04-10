from Estaciones import *


class Bus:
    def __init__(self):
        self.pasajeros = []
        self.capacidad = 15

    def recoger_pasajeros(self, estacion):
        if len(self.pasajeros) + estacion.no_pasajeros <= self.capacidad:
            count = 0
            for i in range(estacion.no_pasajeros):
                self.pasajeros.append(f'pasajero {i}')
                count += 1
            estacion.no_pasajeros = 0
            print(f"Pasajeros recogido en {estacion.nombre}: {count}")
        else:
            pasajerosPorFuera = abs((len(self.pasajeros) + estacion.no_pasajeros) - self.capacidad)
            pasajerosParaBordar = abs(pasajerosPorFuera - estacion.no_pasajeros)
            count = 0
            for i in range(pasajerosParaBordar):
                self.pasajeros.append(f'pasajero {i}')
                count += 1
            estacion.no_pasajeros = pasajerosPorFuera
            print(f"Pasajeros recogido en {estacion.nombre}: {count}")

    def definir_ruta(self, bus, ciudad, estacion_inicio):
        c_inicio = estacion_inicio
        while len(bus.pasajeros) <= self.capacidad:
            if len(bus.pasajeros) == self.capacidad:
                print("\nDevolviendose porque la capacidad esta al maximo")
                print("\nPasajeros Restantes:")
                self.pasajeros_restantes(ciudad, bus)
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
                    estacion_siguiente = a
            self.definir_ruta(bus, ciudad, estacion_siguiente)
        return "Ruta finalizada"

    # Dejar pasajeros en Guadalajara

    def definir_ruta2(self, bus, ciudad, estacion_inicio):
        c_inicio = estacion_inicio
        arreglo_estaciones = []
        keys = []
        for i in ciudad.estaciones:
            keys.append(i)
        for key in keys:
            arreglo_estaciones.append(ciudad.estaciones[key])
        self.bubble_sort(arreglo_estaciones)

        for est in arreglo_estaciones:
            print(f"{est.nombre}, numero pasajeros: {est.no_pasajeros}")

        for ruta in ciudad.rutas:
            if ruta.estacion_inicio == c_inicio and ruta.estacion_destino == arreglo_estaciones[0]:
                self.recoger_pasajeros(arreglo_estaciones[0])
                c_inicio = arreglo_estaciones[0]
                arreglo_estaciones.pop(0)
                print(f"Capacidad del bus: {bus.pasajeros}")
            else:
                print(f"No se")

    def bubble_sort(self, array):
        n = len(array)

        for i in range(n):

            # loop to compare array elements
            for j in range(0, n - i - 1):

                # compare two adjacent elements
                # change > to < to sort in descending order
                if array[j].no_pasajeros > array[j + 1].no_pasajeros:
                    # swapping elements if elements
                    # are not in the intended order
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

    def pasajeros_restantes(self, ciudad, bus):
        keys = []
        for estacion in ciudad.estaciones:
            keys.append(estacion)

        for key in keys:
            if key != 'G':
                print(f"{ciudad.estaciones[key].nombre} --> {ciudad.estaciones[key].no_pasajeros}")
        ciudad.estaciones['G'].pasajeros_llegada = bus.pasajeros
        print(f"\npasajeros en la estacion de llegada:")
        print(ciudad.estaciones['G'].pasajeros_llegada)

    def encontrar_camino(self, inicio, arr_rutas, camino_actual=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.estaciones.get(inicio)
        destino = arr_rutas[0]
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.recoger_pasajeros(inicio)
            arr_rutas.pop(0)
            self.encontrar_camino(destino, camino_actual[:], )
            self.mostrar_camino(camino_actual)
            return
        for ruta in self.rutas:
            if ruta.estacion_inicio == inicio and ruta.estacion_destino not in camino_actual:
                self.encontrar_camino(ruta.estacion_destino, destino, camino_actual[:])
