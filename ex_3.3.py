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

'''
----------------
SCORE CALCULATOR
----------------
'''
time.sleep(1.5)

while True:

    s = input("Enter score here: ")

    try:
        s = float(s)

        if 0 <= s <= 1.0:
            if s >= 0.9:
                print('You have attained an A.')
            elif s >= 0.8:
                print('You have attained a B.')
            elif s >= 0.7:
                print('You have attained a C.')
            elif s >= 0.6:
                print('You have attained a D.')
            else:
                print('You have attained a F grade.')

        else:
            print("Error: Enter a score between 0.0 and 1.0")
            continue

    except:
        print("Error: Please enter a numeric value.")
        continue

    break
