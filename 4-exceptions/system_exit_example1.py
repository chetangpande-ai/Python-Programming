#program termination without error- SystemExit example
val = input("Enter values 0 to start and 1 to exit : ")

if val == '0':
    try:
        value1 = int(input("Enter a number: "))
    except:
        print("Invalid input. Please enter a valid integer again with diff input")
        raise SystemExit("Error occured.")
elif val == '1':
    raise SystemExit("Closing the application as per user request")


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