from fabrica import * 

if __name__ == "__main__":
    operarios = [Operario(f"Operario-{i}") for i in range(4)]
    embotelladores = [Embotellador(f"Embotellador-{i}") for i in range(2)]

    for o in operarios:
        o.start()
    for e in embotelladores:
        e.start()

    for o in operarios:
        o.join()
    for e in embotelladores:
        e.join()


