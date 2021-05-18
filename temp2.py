import time

def suffix():
    if i+1 == 1:
        print('st')
    elif i+1 == 2:
        print('nd')
    else:
        print('rd')


print('-----------------------------')
print('What is the greatest number?')
print('-----------------------------')

non = input('How many numbers would you like to compare? ')
non = int(non)
print('You would like to compare', non, 'numbers.') # non is the number of numbers the user will input.
time.sleep(0.3)

# Create a list to hold all the numbers the user inputs.
numbers = []

# Collect numbers.
for i in range(non):
    non_index = i+1 # type is integer
    non_index = str(non_index)
    # print(type(non_index))
    input_str = input('Please enter your', non_index + suffix(), 'number. ') # does input only allow 1 string?
    input_str = input('Please enter one number. ')
    # print(input_str)
    # input_str = int(input_str)
    # print(type(input_str))
    try:
        numbers.append(input_str)
    except:
        print("Please enter a valid number.")
        continue

# Verify numbers.
while True:

    print('You entered:', numbers)
    chk = input('Are these all the numbers you would like to include? ')

    if chk == 'no':
        chk2 = input('How many numbers do you have remaining? ')
        for i in range(chk2):
            print(i+1)
            new = input('Please enter your', str(i+1) + suffix(), ' additional number. ')
            new = float(new)
            numbers.insert(-1, new)
            print(numbers)
            continue

#    elif chk == 'yes':

#        print("Please enter 'yes' or 'no'. ")
#        continue
