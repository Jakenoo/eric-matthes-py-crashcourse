#2/20/2024; an example from chapter 10
from pathlib import Path
import json

#stores username in .json if one was not found
def create_user(path):
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)

#retrieves stored username in .json if one was found
def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """Greet the user by name"""
    path = Path('username.json')
    username = get_stored_user(path)
    if username:
        print(f"Welcome {username}!")
    else:
        create_user(path)
        print(f"Thank you!")

greet_user()