class Vehicle:
    def __init__(self, brand, price, model):
        self.brand = brand
        self.price = price
        self.model = model


class GasCar(Vehicle):
    def __init__(self, brand, price, model):
        super().__init__(brand, price, model)

    def calculate_tax(self):
        return self.price * 0.15

    def get_fuel_efficiency(self):
        return "Runs on petrol/diesel, moderate fuel efficiency"


class ElectricCar(Vehicle):
    def __init__(self, brand, price, model):
        super().__init__(brand, price, model)

    def calculate_tax(self):
        return 0

    def get_fuel_efficiency(self):
        return "Runs on battery, zero emissions, high efficiency"


if __name__ == "__main__":
    fleet_list = [
        GasCar("Toyota", 3000000, "Corolla"),
        ElectricCar("Tesla", 8000000, "Model 3"),
    ]

    for car in fleet_list:
        print(f"{car.brand} {car.model} -> Tax: {car.calculate_tax()}, {car.get_fuel_efficiency()}")
