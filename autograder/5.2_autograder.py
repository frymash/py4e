largest = None
smallest = None


while True:
    nstr = input("Enter a number: ")

    try:
        if nstr == "done":
            break

        num = int(nstr)

        if largest is None:
            largest = num

        if smallest is None:
            smallest = num

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

        print(largest, smallest)

    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
