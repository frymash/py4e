# Here, we'll calculate someone's gross pay based on the hours they work
# and how much they are paid for their work each hour.

# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate
# for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75).

import time

'''
--------------
PAY CALCULATOR
--------------
'''

while True:
    # The program begins by collecting input (hours, pay per hour) from the user.
    h = input('How many hours do you work? ')

    # Afterwards, the program tries to convert the input from strings to floating-point numbers
    # before printing the result. If the input is invalid, an exception will be made and the
    # program will try again.
    try:
        h = float(h)
    except:
        print("Error; please provide numeric input.")
        continue


    rph = input('How much are you paid for each hour you work? ')
    try:
        rph = float(rph)
    except:
        print("Error; please provide numeric input.")
        continue

    gp =  h * rph
    print('So your gross pay is', gp)
    time.sleep(1)

    print(
    'Let us assume that you are paid the hourly rate up till the 40th hour and 1.5 times the hourly rate for all hours worked above 40 hours.')
    time.sleep(1)

    if float(h) > 40:
        # gp = pay for first 40 hours worked + pay for hours worked after the 40th hour
        new_gp = (40 * float(rph)) + ((float(h) - 40) * (1.5 * float(rph)))
        print("In that case, your gross pay will rise to", new_gp)

    else:
        print('However, since you worked for 40 hours or less, your gross pay will remain at', gp)
    break
