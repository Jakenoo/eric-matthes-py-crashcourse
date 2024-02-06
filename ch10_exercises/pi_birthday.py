# 2/6/2024; an adaptation of file_reader.py
from pathlib import Path

path = Path("C:/Users/jvcp1/Desktop/temppy/ch10_exercises/pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
# for loop reassigns each line in .txt file as one single line stored in contents
for line in lines:
    pi_string += line

birthday = input("Enter your birthday in the form of: mmddyy\n")
pi_iterator = ''
i = 0
# loop iterates through first million digits of pi, verifying if 6-digit
# birthday (mmddyy) is anywhere in there
while i < len(pi_string)-5:
    pi_iterator = pi_string[i:i+6]
    if pi_iterator == birthday:
        print(f"Your birthday is in there! It begins at the {i+1}th digit.")
        break
    i += 1
if pi_iterator != birthday:
    print("Your birthday is not in the first million digits of pi.")