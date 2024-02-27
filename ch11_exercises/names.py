#2/27/2024; another example from chapter 11
from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")
while True:
    #prompting for first, middle, and last names before printing
    first = input("\nPlease give me a first name:")
    if first.lower() == 'q':
        break
    middle = input("\nPlease give me a middle name (press 'enter' to omit this.)")
    if middle.lower() == 'q':
        break
    last = input("\nPlease give me a last name:")
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\nYour name is: {formatted_name}.")