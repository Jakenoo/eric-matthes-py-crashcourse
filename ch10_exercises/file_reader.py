# 2/6/2024; a short example shown in pages 184-189
from pathlib import Path

path = Path("C:/Users/jvcp1/Desktop/temppy/ch10_exercises/pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
# for loop reassigns each line in .txt file as one single line stored in contents
for line in lines:
    pi_string += line

print(f"{pi_string[0:62]}...")
print(len(pi_string))