# 2/13/2024; exercise 10-4
from pathlib import Path

# storing name from user input into contents
name = input("What is your name?\n")

# specifies where to create name.txt and stores data from 'name' into it
path = Path('name.txt')
path.write_text(name)