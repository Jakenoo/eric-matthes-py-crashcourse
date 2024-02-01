# 2/1/2024; just testing we can still call the classes and their methods
from car import Car, ElectricCar

# I don't actually know the exact year of the Stanza in the show
henchman_24_car = Car("nissan", "stanza", 1989)
print(henchman_24_car.get_descriptive_name())

sample_car = ElectricCar("Electric", "Car", 2024)
# There's a method in Battery() for the line below but it was cool figuring out
# this also. Just changes the battery size directly vs using a method to do so
# sample_car.battery.battery_size = 65
sample_car.battery.describe_battery()
sample_car.battery.get_range()

sample_car.battery.upgrade_battery()
sample_car.battery.describe_battery()
sample_car.battery.get_range()