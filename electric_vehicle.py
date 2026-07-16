class Vehicle:
    def __init__(self, price, brand, engine_no):
        self.price = price
        self.brand = brand
        self.engine_no = engine_no


class ElectricCar(Vehicle):
    def __init__(self, price, brand, engine_no, battery_capacity, charging_time):
        super().__init__(price, brand, engine_no)
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

    def __repr__(self):
        return (f"ElectricCar(brand={self.brand}, price={self.price}, "
                f"engine_no={self.engine_no}, battery_capacity={self.battery_capacity}, "
                f"charging_time={self.charging_time})")


if __name__ == "__main__":
    car = ElectricCar(25000, "Tesla", "EV909", "100kWh", "4 hours")
    print(car)
