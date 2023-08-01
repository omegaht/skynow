class Estado:
    def __init__(self, state_name, state_capital, population, area):
        self.state_name = state_name
        self.state_capital = state_capital
        self.population = population
        self.area = area

    def __str__(self):
        return f"{self.state_name} (Capital: {self.state_capital})"
