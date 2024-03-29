# Updated 1/27/2024 according to instructions from exercise 9-4
class Restauraunt:
    """A simple attempt to simulate a restauraunt"""

    def __init__(self, restauraunt_name, cuisine_type):
        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restauraunt(self):
        print(f"{self.restauraunt_name} is a {self.cuisine_type} restauraunt.")
    def open_restauraunt(self):
        print(f"{self.restauraunt_name} is open!")
    
    # block of methods sets number of customers served and prints the information
    def set_number_served(self, customers_served):
        self.number_served = customers_served
    def increment_number_served(self, increment_customers_served):
        self.number_served += increment_customers_served
    def total_served(self):
        print(f"{self.restauraunt_name} has served: {self.number_served}")

# mex_restauraunt = Restauraunt("J & R Tacos", "Mexican")
# mex_restauraunt.describe_restauraunt()
# mex_restauraunt.open_restauraunt()
restauraunt = Restauraunt("Generic Restauraunt", "N/A")
restauraunt.set_number_served(58)
restauraunt.increment_number_served(10)
restauraunt.total_served()