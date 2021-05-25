s = input("Enter score here: ")
try:
    s = float(s)

    if 0 <= s <= 1.0:
        if s >= 0.9:
            print('A')
        elif s >= 0.8:
            print('B')
        elif s >= 0.7:
            print('C')
        elif s >= 0.6:
            print('D')
        else:
            print('F')

    else:
        print("Error: Enter a score between 0.0 and 1.0")

except:
    print("Error: Please enter a numeric value.")
