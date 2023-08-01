class Pais:
    def __init__(self, location_name, location_capital, population, area, currency, main_language):
        self.location_name = location_name
        self.location_capital = location_capital
        self.population = population
        self.area = area
        self.currency = currency
        self.main_language = main_language
        self.estados = []

    def agregar_estado(self, estado):
        self.estados.append(estado)

    def agregar_datos_climaticos(self, temperatura, humedad, velocidad_viento):
        self.datos_climaticos = {
            'temperatura': temperatura,
            'humedad': humedad,
            'velocidad_viento': velocidad_viento
        }

    def __str__(self):
        estados_str = ", ".join([str(estado) for estado in self.estados])
        return f"{self.location_name} (Capital: {self.location_capital}) - Estados: {estados_str}"
