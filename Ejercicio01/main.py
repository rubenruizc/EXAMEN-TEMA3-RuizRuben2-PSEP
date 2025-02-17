from fabrica import *

if __name__ == "__main__":
    fabrica = Fabrica()
    operarios = [Operario(f"Operario-{i}") for i in range(3)]
    
    fabrica.start()
    for o in operarios:
        o.start()
    
    fabrica.join()
    for o in operarios:
        o.join()