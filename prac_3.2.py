rawstr = input('Enter something and Python will tell you if it is a number:')
try:
    num = float(rawstr) # Necessary since all inputs are registered as strings.
except:
    num = 'string'

if type(num) == float:
    print("It's a number.")
else:
    print("Not a number.")

# rawstr = input('Enter something and Python will tell you if it is a natural number:')
# try:
#     num = int(rawstr)
# except:
#     num = -1

# if num > 0:
#     print("It's a natural number.")
# else:
#     print("Not a natural number.")
