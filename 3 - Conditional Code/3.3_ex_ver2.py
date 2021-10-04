# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

import time

print('-------------------')
print('SCORE CALCULATOR v2')
print('-------------------')
time.sleep(1.1)

def gradeConv(s):
    if s >= 0.9:
        return 'A'
    elif s >= 0.8:
        return 'B'
    elif s >= 0.7:
        return 'C'
    elif s >= 0.6:
        return 'D'
    else:
        return 'F'

while True:

    s = input("Enter score here: ")

    try:
        s = float(s)
        if 0 <= s <= 1.0:
            print('You have attained a', gradeConv(s), 'grade.')
        else:
            print("Error: Enter a score between 0.0 and 1.0")
            continue

    except:
        if s == 'yes':
            print('Yes.')
            time.sleep(0.5)
            print('Now re-enter your score.')
            continue

        elif s == 'quit':
            print('Quitting...')
            time.sleep(1.1)
            quit()

        else:
            print("Error: Please enter a numeric value.")
            continue

    break
