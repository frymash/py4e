import re

fname = input("Enter file here: ")
if len(fname) < 1:
    fname = 'regex_sum_1221582.txt'
    # Make sure the .txt file is saved in the same directory as the autograder script.
fh = open(fname)
fstr = fh.read()
nums = re.findall('[0-9]+',fstr) # re.findall returns a list containing all matches
# for checking:
# print(nums)

total = 0

for nstr in nums:
    num = int(nstr)
    total += num
print(total)
