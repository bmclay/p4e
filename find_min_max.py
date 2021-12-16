largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except ValueError: #and not all errors!
        print ("Invalid input")
    else: 
        if smallest is None: 
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)