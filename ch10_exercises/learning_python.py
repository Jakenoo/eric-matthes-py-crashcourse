# 2/11/2024; exercise 10-1
from pathlib import Path

# lines 5-7 gather the info from the .txt and store it as a string in 'contents'
path = Path("C:/Users/jvcp1/Desktop/temppy/ch10_exercises/learning_python.txt")
contents = path.read_text()
print(contents)

# loop prints out each item in 'lines' individually
for line in contents.splitlines():
    print(line)