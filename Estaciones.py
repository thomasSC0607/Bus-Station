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

    def mostar_ciudad(self):
        for ruta in self.rutas:
            print(f"{ruta}")

