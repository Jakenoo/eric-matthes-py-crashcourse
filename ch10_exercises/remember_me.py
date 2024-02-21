#2/20/2024; an example from chapter 10. Also modded by exercise 13
from pathlib import Path
import json

#stores username in .json if one was not found
def create_user(path):
        username = input("What is your name? ")
        fav_color = input("What is your favorite color? ")
        user_dict = {"username": f"{username}", "favorite color": f"{fav_color}"}
        contents = json.dumps(user_dict)
        path.write_text(contents)

#retrieves stored username in .json if one was found
def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

#subtask for greet_user (loops through user_info to print)
def print_user_info(user_info):
    print(f"Here's some cool things about you:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

def greet_user():
    """Greet the user by name"""
    path = Path('user_info.json')
    user_info = get_stored_user(path)
    if user_info:
        print_user_info(user_info)
    else:
        create_user(path)
        print(f"Thank you!")

greet_user()