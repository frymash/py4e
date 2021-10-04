# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# start line count and overall sum
lcount = 0
nums = []
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    zero_pos = line.find('0')
    nstr = line[zero_pos:-1]
    num = float(nstr)
    nums.append(num)

for num in nums:
    total += num

avg = total / len(nums)

print("Average spam confidence:", avg)    
