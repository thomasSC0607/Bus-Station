class Estacion:
    def __init__(self, id, nombre, no_pasajeros):
        self.id = id
        self.nombre = nombre
        self.no_pasajeros = no_pasajeros
        self.pasajeros_llegada = []  # El unico que implementa este atributo es la estacion Guadalajara


class Ruta:
    def __init__(self, estacion_inicio, estacion_destino, distancia):
        self.estacion_inicio = estacion_inicio
        self.estacion_destino = estacion_destino
        self.distancia = distancia

    def __str__(self):
        return f'{self.estacion_inicio.nombre} ----> {self.estacion_destino.nombre} :: distacia: {self.distancia} km'


class Ciudad:
    def __init__(self):
        self.estaciones = {}
        self.rutas = []

    def add_estacion(self, estacion):
        self.estaciones[estacion.id] = estacion

    def add_ruta(self, estacion_inicio, estacion_destino, distancia):
        if estacion_inicio.id in self.estaciones and estacion_destino.id in self.estaciones:
            ruta = Ruta(estacion_inicio, estacion_destino, distancia)
            self.rutas.append(ruta)

    def encontrar_todas_las_rutas(self, inicio_id, destino_id, ruta_actual=None, distancia_total=0):
        if ruta_actual is None:
            ruta_actual = []  # Pasa a ser un arreglo vacio
        inicio = self.estaciones.get(inicio_id) # Obtiene el valor de key
        destino = self.estaciones.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        ruta_actual = ruta_actual + [inicio] # Agrega el nodo de inicio a la ruta actual
        if inicio == destino:
            self.mostrar_ruta(ruta_actual, distancia_total)
        else:
            for ruta in self.rutas: #se itera sobre todas las rutas en la lista rutas de la ciudad.
                if ruta.estacion_inicio == inicio and ruta.estacion_destino not in ruta_actual:
                    self.encontrar_todas_las_rutas(ruta.estacion_destino.id, destino_id, ruta_actual[:], #aqui se pasa como ciudad inicio una de las rutasa del nodo actual
                                                   distancia_total + ruta.distancia)

    def mostrar_ruta(self, ruta, distancia_total):
        if ruta:
            print("\nRUTA ENCONTRADA:")
            for i in range(len(ruta) - 1):
                print(f"{ruta[i].nombre} -> {ruta[i + 1].nombre}")
            print(f"Distancia total de la ruta: {distancia_total} km")
            print('-' * 20)

    def mostar_ciudad(self):
        for ruta in self.rutas:
            print(f"{ruta}")



    def mostrar_camino(self, camino):
        if camino:
            print("\nCAMINO ENCONTRADO:")
            costo_total = 0
            for i in range(len(camino) - 1):
                arista = self.buscar_arista(camino[i].id, camino[i + 1].id)
                print(f"{arista.nodo_inicio.nombre} -> {arista.nodo_destino.nombre} (Peso: {arista.peso})")
                costo_total += arista.peso
            print(f"Costo total del camino: [{costo_total} Km]\n")
            print('-'*20)


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



