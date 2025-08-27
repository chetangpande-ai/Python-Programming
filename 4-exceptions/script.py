#python script - py file to demonstrate exception handling
try:
    val_1=int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    print("Setting value to 0.")
    val_1=0

try:
    val_2=int(input("Enter another number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    print("Setting value to 0.")


def addNumbers(a,b):
    return a+b

answer=addNumbers(val_1,val_2)
print("The sum is:", answer)
