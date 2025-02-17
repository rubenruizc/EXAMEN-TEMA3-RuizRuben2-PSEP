import time
import random
from threading import Thread, Lock, Condition

class Tolva:
    capacidad_maxima = 500  # Capacidad máxima en litros
    cantidad_actual = 0  # Cantidad inicial de aceite en la tolva
    lock = Lock()
    condition = Condition(lock)

class Operario(Thread):
    color = "\033[0;31m"

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while True:
            litros = random.randint(5, 30)
            tiempo = litros / 5  # Relación 1/5 (5 litros = 1 segundo)
            
            with Tolva.lock:
                while Tolva.cantidad_actual + litros > Tolva.capacidad_maxima:
                    print(self.color, f"{self.nombre}: La tolva está llena, esperando espacio...")
                    Tolva.condition.wait()
                
                print(self.color, f"{self.nombre}: Añadiendo {litros} litros de aceite a la tolva")
                time.sleep(tiempo)
                Tolva.cantidad_actual += litros
                print(self.color, f"{self.nombre}: He terminado de añadir aceite. Tolva: {Tolva.cantidad_actual}L")
                
                Tolva.condition.notify_all()  # Avisar a los embotelladores que hay más aceite disponible

class Embotellador(Thread):
    color = "\033[0;32m"

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while True:
            with Tolva.lock:
                while Tolva.cantidad_actual < 5:
                    print(self.color, f"{self.nombre}: Esperando aceite suficiente para embotellar...")
                    Tolva.condition.wait()
                
                print(self.color, f"{self.nombre}: Retirando 5 litros de la tolva para embotellado")
                time.sleep(0.5)  # Tiempo de embotellado fijo de 0.5 segundos por botella
                Tolva.cantidad_actual -= 5
                print(self.color, f"{self.nombre}: Embotellado completado. Tolva: {Tolva.cantidad_actual}L")
                
                Tolva.condition.notify_all()  # Avisar a los operarios que hay más espacio disponible