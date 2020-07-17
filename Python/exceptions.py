import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid character entered")
    sys.exit(1)


try:
    result = x/y
except ZeroDivisionError:
    print("Error : cannot divide by 0.")
    sys.exit(1)

print(f"{x}/{y}={result}")

tupleExample = ("Hello",12)

print(tupleExample[0])