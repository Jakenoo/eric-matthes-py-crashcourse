# 2/16/2024; exercise 10-6 and 10-7
# a short exercise to practice using try-except blocks

while True:
    print("Enter 'q' to quit at anytime.")
    firstnum = input("Enter your first choice of integer: ")
    if firstnum == 'q':
        break
    secondnum = input("Enter your second choice of integer: ")
    if secondnum == 'q':
        break

    try:
        ans = int(firstnum) + int(secondnum)
        print(ans)
    except ValueError:
        print("You need to enter integers!")