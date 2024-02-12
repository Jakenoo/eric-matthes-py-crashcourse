# 2/11/2024; exercise 10-2
from pathlib import Path

# lines 5-7 gather the info from the .txt and store it as a string in 'contents'
path = Path("C:/Users/jvcp1/Desktop/temppy/ch10_exercises/learning_python.txt")
contents = path.read_text()
# replace() simply replaces the word 'Python' with 'C' in the string
contents = contents.replace('Python', 'C')
print(contents)