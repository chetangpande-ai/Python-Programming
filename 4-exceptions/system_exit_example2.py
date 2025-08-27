#program termination without error- SystemExit example
import sys
val = input("Enter values 0 to start and 1 to exit : ")

if val == '0':
    try:
        value1 = int(input("Enter a number: "))
    except:
        print("Invalid input. Please enter a valid integer again with diff input")
        raise SystemExit("Error occured.")
elif val == '1':
   sys.exit(0)  # Normal termination
   


def add1():
    print(value1+2)

def add2():
    print(value1+2)

def add3():
    print(value1+2)


add1()
add2()
add3()
add1()
add2()
add3()
add1()
add2()
add3()
add1()
add2()
add3()