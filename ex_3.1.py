# Here, we'll calculate someone's gross pay based on the hours they work
# and how much they are paid for their work each hour.

# The program begins by collecting input (hours, pay per hour) from the user.
import sys
import time

h = input('How many hours do you work? ')
rph = input('How much are you paid for each hour you work? ')

# Afterwards, the program converts the input from strings to
# floating-point numbers before printing the result.
gp =  float(h) * float(rph)
print('So your gross pay is', gp)
# sys.stdout.flush()
time.sleep(2)

# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate
# for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75).
print(
'Let us assume that you are paid the hourly rate up till the 40th hour and 1.5 \
times the hourly rate for all hours worked above 40 hours.')
# sys.stdout.flush()
time.sleep(2)


if float(h) > 40:
    # gp = pay for first 40 hours worked + pay for hours worked after the 40th hour
    ot_gp = (40 * float(rph)) + ((float(h) - 40) * (1.5 * float(rph)))
    print("In that case, your gross pay will rise to", ot_gp)

else:
    print('However, since you worked for 40 hours or less, your gross pay will \
    remain at', gp)
