# 2/13/2024; exercise 10-5
from pathlib import Path

path = Path('guest_book.txt')

names = ''
while True:
    prompt = input("Write as many names as you want. Enter 'q' to quit.\n")
    if prompt == 'q':
        break
    names += prompt + '\n'

path.write_text(names)