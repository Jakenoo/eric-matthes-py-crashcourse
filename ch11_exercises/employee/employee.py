# 22/5/2024; p.223 exercise 11-3

class Employee:
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, annual_raise=5000):
        self.salary = self.salary + annual_raise
        print(f"{self.first_name} {self.last_name} got a raise of " 
              + f"{annual_raise}.")

#jane_doe = Employee('jane', 'doe', 60000)
#jane_doe.give_raise(7000)