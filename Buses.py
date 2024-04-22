from Estaciones import *


class Bus:
    def __init__(self):
        self.pasajeros = []
        self.capacidad = 15

    def encontrar_camino1(self, ciudad, inicio_id, destino_id, arreglo_estaciones, camino_actual=None, ):

        if len(arreglo_estaciones) > 0:

            if camino_actual is None:
                camino_actual = []  # lista
            inicio = ciudad.estaciones.get(inicio_id)
            destino_id = arreglo_estaciones[0].id
            destino = arreglo_estaciones[0]

            camino_actual = camino_actual + [inicio]
            if inicio == destino:
                self.mostrar_camino(ciudad, camino_actual)
                camino_actual = []
                if destino.no_pasajeros != 0:  # Si hay pasajeros, que los recoja
                    self.recoger_pasajeros(destino)
                print("\nPasajeros Restantes en la ciudad:\n")
                self.pasajeros_restantes(ciudad, self)
                if len(self.pasajeros) == self.capacidad:  # Si la capacidad del bus esta al maximo
                    for pasajero in self.pasajeros:
                        ciudad.estaciones['G'].pasajeros_llegada.append(pasajero)
                    ciudad.estaciones['G'].pasajeros_llegada.append(self.pasajeros)
                    print("\nDevolviendose rumbo a guadalajara ya que la capacidad del bus esta al maximo")
                    self.encontrar_camino_guadalajara(ciudad, inicio.id, camino_actual[:])
                    print(
                        f"\nPasajeros que llegaron a Guadalajara: {len(ciudad.estaciones['G'].pasajeros_llegada) - 1}\n")
                    print(f"{ciudad.estaciones['G'].pasajeros_llegada}\n")
                    self.pasajeros = []
                    print("\nPasajeros Restantes en la ciudad:\n")
                    self.pasajeros_restantes(ciudad, self)
                    if ciudad.total_pasajeros() > 0:  # si hay aun en la ciudad
                        ciudad.agregar_pasajeros_ran30(ciudad)
                    print("Estado actual de la ciudad despues de agregar pasajeros random(30%)\n")
                    self.pasajeros_restantes(ciudad, self)
                    self.definir_ruta2(self, ciudad, ciudad.estaciones['M'])
                elif ciudad.total_pasajeros() == 0:  # si ya no hay mas personas en la ciudad
                    for pasajero in self.pasajeros:
                        ciudad.estaciones['G'].pasajeros_llegada.append(pasajero)
                    print("\nYa no hay mas pasajeros Restantes en la ciudad: 😴\n")
                    self.pasajeros_restantes(ciudad, self)
                    print("\nDevolviendose rumbo a guadalajara ya que no hay mas pasajeros en la ciudad 😢\n")
                    self.encontrar_camino_guadalajara(ciudad, inicio.id, camino_actual[:])
                    print(
                        f"\nPasajeros que llegaron a Guadalajara: {len(ciudad.estaciones['G'].pasajeros_llegada) - 1}\n")
                    print(f"{ciudad.estaciones['G'].pasajeros_llegada}\n")
                    print("\n🍑----------------------Ruta finalizada------------------------------🍑\n")
                    print("Gracias por elegirnos como su transportadora de confiaza💕")

                    exit()
                arreglo_estaciones.pop(0)
                if len(arreglo_estaciones) == 0:
                    return
                self.encontrar_camino1(ciudad, inicio_id, destino_id, arreglo_estaciones, camino_actual[:])
                return
            for ruta in ciudad.rutas:
                if len(arreglo_estaciones) == 0:
                    self.encontrar_camino1(ciudad, ruta.estacion_destino.id, 'G', arreglo_estaciones,
                                           camino_actual[:])
                if ruta.estacion_inicio == inicio and ruta.estacion_destino == destino:
                    self.encontrar_camino1(ciudad, ruta.estacion_destino.id, destino_id, arreglo_estaciones,
                                           camino_actual[:])

                if ruta.estacion_inicio.nombre != 'Guadalajara' and ruta.estacion_destino.nombre != 'Guadalajara' and ruta.estacion_inicio == inicio and ruta.estacion_destino not in camino_actual:
                    self.encontrar_camino1(ciudad, ruta.estacion_destino.id, destino_id, arreglo_estaciones,
                                           camino_actual[:])
        else:
            print("No hay estaciones para recoger pasajeros")
            return

    def recoger_pasajeros(self, estacion):
        if len(self.pasajeros) + estacion.no_pasajeros <= self.capacidad:
            count = 0
            for i in range(estacion.no_pasajeros):
                self.pasajeros.append(f'pasajero {i}')
                count += 1
            estacion.no_pasajeros = 0
            print(f"\nBus llego a {estacion.nombre} 🚏")
            print(f"Pasajeros recogido en {estacion.nombre}: {count} 🚌")
        else:
            pasajerosPorFuera = abs((len(self.pasajeros) + estacion.no_pasajeros) - self.capacidad)
            pasajerosParaBordar = abs(pasajerosPorFuera - estacion.no_pasajeros)
            count = 0
            for i in range(pasajerosParaBordar):
                self.pasajeros.append(f'pasajero {i}')
                count += 1
            estacion.no_pasajeros = pasajerosPorFuera
            print(f"\nBus llego a {estacion.nombre} 🚏")
            print(f"Pasajeros recogido en {estacion.nombre}: {count} 🚌")

    def definir_ruta2(self, bus, ciudad, estacion_inicio):
        c_inicio = estacion_inicio
        arreglo_estaciones = []
        keys = []
        for i in ciudad.estaciones:
            if i != 'G':
                keys.append(i)
        for key in keys:
            if ciudad.estaciones[key].no_pasajeros != 0:
                arreglo_estaciones.append(ciudad.estaciones[key])
        self.bubble_sort(arreglo_estaciones)

        bus.encontrar_camino1(ciudad, c_inicio.id, arreglo_estaciones[0].id, arreglo_estaciones)

    def encontrar_camino(self, ciudad, inicio, arr_rutas):
        destino = arr_rutas[0]
        if inicio == destino:
            self.recoger_pasajeros(inicio)
            arr_rutas.pop(0)
            self.encontrar_camino(ciudad, destino, arr_rutas)
            return
        for ruta in ciudad.rutas:
            if ruta.estacion_inicio == inicio and ruta.estacion_destino not in arr_rutas:
                self.encontrar_camino(ciudad, ruta.estacion_destino, destino)

    def encontrar_camino_guadalajara(self, ciudad, inicio_id, camino_actual=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = ciudad.estaciones.get(inicio_id)
        destino_id = 'G'  # 'G' es el id de Guadalajara
        destino = ciudad.estaciones.get(destino_id)

        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            self.mostrar_camino(ciudad, camino_actual)
            return camino_actual
        for ruta in ciudad.rutas:
            if ruta.estacion_inicio == inicio and ruta.estacion_destino not in camino_actual:
                camino = self.encontrar_camino_guadalajara(ciudad, ruta.estacion_destino.id, camino_actual[:])
                if camino:  # Si se encontró un camino, se retorna inmediatamente
                    return camino
        return None  # Si no se encontró ningún camino, se retorna None

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

    def mostrar_camino(self, ciudad, camino):  # camino siendo el, arreglo de nodos
        if camino:
            print(f"\nSiguiemte parada {camino[-1].nombre} 🫷")
            print("\nRuta encontrada:👌")
            costo_total = 0
            for i in range(len(camino) - 1):
                ruta = self.buscar_rutaa(ciudad, camino[i].id, camino[i + 1].id)
                print(f"{ruta.estacion_inicio.nombre} -> {ruta.estacion_destino.nombre} (Distancia: {ruta.distancia})")
                costo_total += ruta.distancia
            print(f"Costo total del camino:🤑 [{costo_total} Km]\n")
            print('-' * 20)

    def buscar_rutaa(self, ciudad, inicio_id, destino_id):
        for ruta in ciudad.rutas:
            if ruta.estacion_inicio.id == inicio_id and ruta.estacion_destino.id == destino_id:
                return ruta
