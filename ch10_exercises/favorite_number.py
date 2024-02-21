#2/20/2024; exercise 10-11
# This is really the same program as the example in the last section of ch 10

from pathlib import Path
import json

def store_favorite_number(path):
    favorite_num = input("What is your favorite number? ")
    path.write_text(json.dumps(favorite_num))
    print(f"Your favorite number ({favorite_num}) has been stored.")

def get_favorite_number(path):
    favorite_num = json.loads(path.read_text())
    print(f"Your favorite number is {favorite_num}!")

def read_favorite_number():
    path = Path("favorite_number.json")
    if path.exists():
        get_favorite_number(path)
    else:
        store_favorite_number(path)

read_favorite_number()