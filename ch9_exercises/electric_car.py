# 1/29/2024; file originally written by Eric Matthes
class Car:
    """class representing a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """set new odometer reading. reject if it tries to roll back number"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No changes made; odometer can't be rolled back.")
    def increment_odometer(self, miles):
        """increase odometer reading by specified amount"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """subclass of Car superclass for electric cars"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    """Battery class working together with ElectricCar class"""
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery size: {self.battery_size}")
    def upgrade_battery(self):
        """changes battery size to 65 if it is not already"""
        if self.battery_size != 65:
            print("Changing battery size to 65.")
            self.battery_size = 65
        else:
            print("Battery size is already at 65.")
    def get_range(self):
        """print the range the battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"The battery range can handle approx. {range} miles.")

sample_car = ElectricCar("Electric", "Car", 2024)
# there's a method for the line below but it was cool figuring out this also
# sample_car.battery.battery_size = 65
sample_car.battery.describe_battery()
sample_car.battery.get_range()

sample_car.battery.upgrade_battery()
sample_car.battery.describe_battery()
sample_car.battery.get_range()