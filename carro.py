class Carro:
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.pasajeros = pasajeros
        self.combustible = combustible

    # Métodos comunes
    def arrancar(self):
        return f"El carro {self.modelo} está encendido."

    def apagar(self):
        return f"El carro {self.modelo} se apagó."

    def acelerar(self):
        return f"El carro {self.modelo} está acelerando."

    def frenar(self):
        return f"El carro {self.modelo} está frenando."

    def luces(self):
        return f"Luces del carro {self.modelo} encendidas."

    def ventanas(self):
        return f"Ventanas del carro {self.modelo} abiertas."

    def espejos(self):
        return f"Ajustando espejos del carro {self.modelo}."

    def informacion(self):
        return (
            f"Modelo: {self.modelo}, Color: {self.color}, Motor: {self.motor}, "
            f"Puertas: {self.puertas}, Pasajeros: {self.pasajeros}, "
            f"Combustible: {self.combustible}"
        )


# -----------------------------
# CLASES HIJAS
# -----------------------------

class CarroDeportivo(Carro):
    def __init__(self, modelo, color, motor):
        super().__init__(modelo, color, motor, 2, 2, "Gasolina")


class CarroVan(Carro):
    def __init__(self, modelo, color, motor):
        super().__init__(modelo, color, motor, 4, 12, "Diesel")


class CarroCamion(Carro):
    def __init__(self, modelo, color, motor):
        super().__init__(modelo, color, motor, 2, 3, "Diesel")
