class BaseCarros:
    def __init__(self):
        self.lista_carros = []
        self.deportivos = []
        self.vans = []
        self.camiones = []

    def agregar_carro(self, carro):
        self.lista_carros.append(carro)

        # Clasificación automática
        if type(carro).__name__ == "CarroDeportivo":
            self.deportivos.append(carro)
        elif type(carro).__name__ == "CarroVan":
            self.vans.append(carro)
        elif type(carro).__name__ == "CarroCamion":
            self.camiones.append(carro)

    def imprimir_info(self):
        for carro in self.lista_carros:
            print(carro.informacion())
            print(carro.arrancar())
            print("-" * 40)
