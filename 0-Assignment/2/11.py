inp = int(input("Enter a number: "))
factorial = 1
for i in range(1, inp + 1):
    factorial *= i
print(f"The factorial of {inp} is {factorial}")