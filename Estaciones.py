import random


class Estacion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.no_pasajeros = 0
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

    def total_pasajeros(ciudad):
        total = 0
        for estacion in ciudad.estaciones.values():
            total += estacion.no_pasajeros
        return total

    def distribuir_pasajeros(self, num_pasajeros):
        import random
        estaciones = []
        for estacion in self.estaciones.values():
            if estacion.id != 'G':
                estaciones.append(estacion)
        while num_pasajeros > 0:
            estacion = random.choice(estaciones)
            estacion.no_pasajeros += 1
            num_pasajeros -= 1

    def agregar_pasajeros_ran30(self, ciudad):
        total_pasajeros_agregados = 0
        for estacion in ciudad.estaciones.values():
            if estacion.id != 'G':
                if total_pasajeros_agregados >= 15:
                    break
                if random.random() <= 0.3:  # 30% de probabilidad de agregar pasajeros ya que el random genera de 0 a 1
                    estacion.no_pasajeros += 1
                    total_pasajeros_agregados += 1

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

    def mostrar_camino(self, camino): #camino siendo e, arreglo de nodos
        if camino:
            print("\nCAMINO ENCONTRADO:")
            costo_total = 0
            for i in range(len(camino) - 1):
                arista = self.buscar_arista(camino[i].id, camino[i + 1].id)
                print(f"{arista.nodo_inicio.nombre} -> {arista.nodo_destino.nombre} (Peso: {arista.peso})")
                costo_total += arista.peso
            print(f"Costo total del camino: [{costo_total} Km]\n")
            print('-'*20)

    def buscar_ruta(self, inicio_id, destino_id):
        for ruta in self.rutas:
            if ruta.estacion_inicio.id == inicio_id and ruta.estacion_destino.id == destino_id:
                return ruta
