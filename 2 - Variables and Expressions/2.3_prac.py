# In Europe, building floors typically start counting from 0 while American floor numbers begin from 1.
# Create a program which is able to receive European floor numbers as input before converting them to American floor numbers.
eu_f = input('European floor: ')
# The input assigned to eu_f will be saved as a string.
# However, mathematical operations cannot be performed on strings.
# For addition to be possible, eu_f will need to be converted into an integer.
us_f = int(eu_f) + 1
print('US floor:', us_f)
