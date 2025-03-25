numone =int(input("Enter the first number: "))
numtwo = int(input("Enter the second number: "))
operation = input("Enter the operation: ")

def add(numone,numtwo):
    print(numone+numtwo)
def subtract(numone,numtwo):
    print(numone-numtwo)
def multiply(numone,numtwo):
    print(numone*numtwo)
def divide(numone,numtwo):
    print(numone//numtwo)


if operation == "+":
    add(numone, numtwo)
elif operation =="-":
    subtract(numone,numtwo)
elif operation =="*":
    multiply(numone,numtwo)
elif operation =="/":
    divide(numone,numtwo)
else:
    print("invalid operation")



