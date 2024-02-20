# 2/19/2024; exercise 10-8. Had to look this one up, so my code here
# is not solely mine but something I wrote with help from Matthes' solutions

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, but '{filename}' does not exist.")
    else:
        print(f'This is the content in: {path}')
        print(contents)