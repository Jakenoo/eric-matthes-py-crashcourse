#2/20/2024; an example from chapter 10. Also modded by exercise 13
#2/25/2024; modded by exercise 14
from pathlib import Path
import json

def create_user(path):
    """stores username in .json if one was not found"""
    username = input("What is your name? ")
    fav_color = input("What is your favorite color? ")
    user_dict = {"username": f"{username}", "favorite color": f"{fav_color}"}
    contents = json.dumps(user_dict)
    path.write_text(contents)


def get_stored_user(path):
    """retrieves stored username in .json if one was found"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def print_user_info(user_info):
    """subtask for greet_user (loops through user_info to print)"""
    print(f"Hi {user_info["username"].title()}! \nHere's some cool things about you:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

def check_username(username, path):
    """verifies user's info via input; terminates session if invalid. needs a path"""
    if username.lower() != "y":
            create_user(path)
            print("We'll get that right next time!")

            #quits before displaying incorrect user info
            quit()

def greet_user():
    """Greet the user by name"""
    path = Path('user_info.json')
    user_info = get_stored_user(path)

    username = input(f"Is your name {user_info["username"]}? (enter 'y' if correct)")
    check_username(username, path)

    #prints user info, or creates/rewrites file storing info
    if user_info:
        print_user_info(user_info)
    else:
        create_user(path)
        print("Thank you!")

greet_user()