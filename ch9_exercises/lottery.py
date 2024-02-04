# 2/3/2024; exercise 9-14, 15
# Just a silly lottery simulator. Fun mini-project though

from random import choice
sample_char = [2, 3, 5, 2, 1, 7, 2, 9, 't', 'q']
winning_codes = ["213t", "5912", "q111", "1729", "1359"]

drawn_code = ""
# This block below was originally for running the same once
# While loop for one-time games
# while len(drawn_code) < 4:
#     drawn_code = drawn_code + str(choice(sample_num))
# print(f"Here is your draw: {drawn_code}")

i = 1
while drawn_code not in winning_codes:
    drawn_code = drawn_code + str(choice(sample_char))
    if i % 5 == 0:
        drawn_code = ""
    i += 1

# Printing i-1, since I couldn't figure out how to get the modulo operator to
# work with i = 0 well
print(f"You won! It took {i-1} draws to get here! Your winning code was " + 
      f"{drawn_code}")

# Verifying if drawn code is a winning code
# if drawn_code in winning_codes:
#     print("Congrats, you won!")
# else:
#     print("Whomp whomp.")