from carro import CarroDeportivo, CarroVan, CarroCamion
from base_datos import BaseCarros

def main():
    base = BaseCarros()

    # Crear objetos
    deportivo = CarroDeportivo("BMW M2", "Negro", "3.0 Turbo")
    van = CarroVan("Chevrolet N300", "Blanco", "1.5")
    camion = CarroCamion("Kenworth T800", "Beige", "TurboDiesel 15L")

    # Agregar a la base
    base.agregar_carro(deportivo)
    base.agregar_carro(van)
    base.agregar_carro(camion)

    # Imprimir información general
    base.imprimir_info()

    # Clasificación
    print("=== CARROS DEPORTIVOS ===")
    for c in base.deportivos:
        print(c.modelo)

    print("\n=== VANS ===")
    for c in base.vans:
        print(c.modelo)

    print("\n=== CAMIONES ===")
    for c in base.camiones:
        print(c.modelo)


if __name__ == "__main__":
    main()
