import time
import random
from threading import Thread, Lock, Condition

class Fabrica(Thread):
    listaAtomos = ["H", "O"]
    lock = Lock()
    condition = Condition(lock)
    atomos_generados = []
    moleculas_creadas = 0

    def run(self):
        while True:
            with Fabrica.lock:
                atomo = random.choice(Fabrica.listaAtomos)
                Fabrica.atomos_generados.append(atomo)
                print(f"La fábrica ha generado un átomo de {atomo}")
                Fabrica.condition.notify_all()
            time.sleep(1)

class Operario(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre
        self.listaAtomosConseguidos = []

    def run(self):
        while True:
            self.listaAtomosConseguidos = []  # Vaciar lista después de ensamblar una molécula
            while len(self.listaAtomosConseguidos) < 3:
                with Fabrica.lock:
                    while len(Fabrica.atomos_generados) < 1:
                        Fabrica.condition.wait()
                    
                    atomo = Fabrica.atomos_generados.pop(0)
                    self.listaAtomosConseguidos.append(atomo)
                    print(f"El operario {self.nombre} ha obtenido un átomo de {atomo}")
                time.sleep(1)
                
            if self.listaAtomosConseguidos.count("H") >= 2 and self.listaAtomosConseguidos.count("O") >= 1:
                self.listaAtomosConseguidos.remove("H")
                self.listaAtomosConseguidos.remove("H")
                self.listaAtomosConseguidos.remove("O")
                with Fabrica.lock:
                    Fabrica.moleculas_creadas += 1
                    print(f"{self.nombre} ha ensamblado una molécula de H2O. Total: {Fabrica.moleculas_creadas}")
                    Fabrica.condition.notify_all()
                time.sleep(1)