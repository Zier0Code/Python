import sys


try:
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
except ValueError:
    print("Wrong Input Value")
    sys.exit(1)

try:
    result = x / y
except:
    print("Cannot be divided by Zero")
    sys.exit(1)

print(f"The division of {x} and {y} is equal to {round(result, 2)}")

