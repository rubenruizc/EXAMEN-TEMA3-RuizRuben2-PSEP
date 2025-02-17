import time
import random
from threading import Thread,Lock

listaAtomos = ["H","O"]
class Fabrica(Thread):
 

    def __init__ (self):
        Thread.__init__(self)
        self.atomo = random.choice(listaAtomos)

    def run (self):
        while True:
            print("La fábrica ha generado un átomo de ", self.atomo)
            time.sleep(2)
    
        

    


class Operario(Thread):
    
    lock = Lock()

    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre = nombre
        self.listaAtomosConseguidos = []

    def run(self):
        with Operario.lock:
            print("El operario",self.nombre,"ha obtenido un átomo de:",Fabrica.atomo)
            self.listaAtomosConseguidos.append(Fabrica.atomo)

        


