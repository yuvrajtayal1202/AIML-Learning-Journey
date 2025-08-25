input = int(input("Enter a number: "))
if input >0:
    print("Positive")
    if input %2 == 0:
        print("Even")    
    else:
        print("Odd")
elif input == 0:
    print("Zero")
else:
    print("Negative or Zero")