# 1/29/2024; module for Admin subclass of User superclass
import user
class Admin(user.User):
    def __init__(self, first_name, last_name, age, birthday):
        super().__init__(first_name, last_name, age, birthday)
        self.privileges = ["can add post", "can delete post", "can ban user", 
                           "can make announcements"]
    def show_privileges(self):
        print("Here are the current privileges for admins:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

first_admin = Admin("Captain", "Qwark", "n/a", "11/04/2002")
first_admin.show_privileges()