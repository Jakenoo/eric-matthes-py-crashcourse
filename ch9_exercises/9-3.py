# 1/28/2024; a short exercise from the section on classes (p. 162)
# updated the same date according to exercise 9-5 instructions

class User:
    """A short user class maybe simulating a profile on a website"""
    def __init__(self, first_name, last_name, age, birthday):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.birthday = birthday
        self.login_attempts = 0
    def describe_user(self):
        print(f"Here is information on {self.first_name} " + 
              f"{self.last_name}:")
        print(f"Age: {self.age}\nBirthday: {self.birthday}")
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
    
    # block for login-related data
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("mr", "michi", 2, "02/28/2023")
user1.greet_user()
user1.describe_user()

user2 = User("mrs", "puff", 40, "08/07/1999")
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)