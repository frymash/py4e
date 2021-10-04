text = "X-DSPAM-Confidence:    0.8475"
zero_pos = text.find("0")
# index of '0' is 23
nstr = text[zero_pos:]
num = float(nstr)
print(num)
