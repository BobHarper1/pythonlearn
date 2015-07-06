largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        int(num)
        if num is None or num > largest:
            largest = num
        if num is largest or num < smallest:
            smallest = num
    except:
        print 'Invalid input'
        if num == "done":
            break
print "Maximum is", largest, "Minimum is", smallest
