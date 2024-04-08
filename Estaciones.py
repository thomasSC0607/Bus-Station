class Estacion:
    def __init__(self, id, nombre, pasajeros):
        self.id = id
        self.nombre = nombre
        self.pasajeros = pasajeros


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

