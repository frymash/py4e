# Prompt user for hours and rate per hour
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
rph = float(rate)


# Pay the hourly rate for the hours up to 40
# and 1.5 times the hourly rate for all hours
# worked above 40 hours.

if h <= 40:
    gp = h*rph
elif h > 40:
    gp = (40*rph)+((h-40)*rph*1.5)

print(gp)
