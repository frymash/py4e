# computepay():
# - Pay the normal rate for hours up to 40 .
# - 1.5x pay for all hours worked above 40 hours.

def computepay(h, r):
    hrs = float(h)
    rph = float(r)
    if hrs <= 40:
        gp = hrs*rph
    elif hrs > 40:
        gp = (40*rph)+((hrs-40)*rph*1.5)
    return gp

h = input("Enter Hours:")
r = input("Enter rate per hour:")
p = computepay(h, r)

print("Pay", p)
