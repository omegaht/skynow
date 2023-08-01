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

    def obtener_datos_paises_desde_api():
        url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json"
        response = requests.get(url)
        datos_paises = response.json()
        return datos_paises

    def _obtener_datos_estados_desde_api(self):
        url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-states-api.json"
        response = requests.get(url)
        datos_estados = response.json()
        return datos_estados
    
    def obtener_datos_climaticos_desde_api():
        url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json"
        response = requests.get(url)
        datos_climaticos = response.json()
        return datos_climaticos
    
   def cargar_datos():
    datos_paises = obtener_datos_paises_desde_api()
    datos_estados = obtener_datos_estados_desde_api()
    datos_climaticos = obtener_datos_climaticos_desde_api()

    paises = []
    for datos_pais in datos_paises:
        pais = Pais(
            datos_pais["location_name"],
            datos_pais["location_capital"],
            datos_pais["population"],
            datos_pais["area"],
            datos_pais["currency"],
            datos_pais["main_language"]
        )

        for datos_estado in datos_estados:
            if datos_estado["location_name"] == datos_pais["location_name"]:
                for estado in datos_estado["location_states"]:
                    estado_obj = Estado(
                        estado["state_name"],
                        estado["state_capital"],
                        estado["population"],
                        estado["area"]
                    )
                    pais.agregar_estado(estado_obj)

        # Obtenemos los datos climáticos del país
        for datos_climatico in datos_climaticos:
            if datos_climatico["location_name"] == pais.location_name:
                for medida_climatica in datos_climatico["location_measurements"]:
                    temperatura = medida_climatica["temperature"]
                    humedad = medida_climatica["humidity"]
                    velocidad_viento = medida_climatica["wind_speed"]
                    fecha = medida_climatica["date"]

                    pais.agregar_datos_climaticos(temperatura, humedad, velocidad_viento, fecha)

        paises.append(pais)

    return paises


    def mostrar_informacion_paises(paises):
        for pais in paises:
            print(pais)
            for estado in pais.estados:
                print(f"   - {estado}")
            for medida_climatica in pais.datos_climaticos:
                print(f"Datos climáticos: {medida_climatica}")
            print()

    def __str__(self):
        estados_str = ", ".join([str(estado) for estado in self.estados])
        return f"{self.location_name} (Capital: {self.location_capital}) - Estados: {estados_str}"

